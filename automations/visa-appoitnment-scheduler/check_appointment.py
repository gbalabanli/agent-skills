#!/usr/bin/env python3
"""US visa appointment availability checker with per-run logging and email alerts.

Usage examples:
  python automations/visa-appoitnment-scheduler/check_appointment.py --check-live
  python automations/visa-appoitnment-scheduler/check_appointment.py --status available

Environment variables (for email):
  SMTP_HOST, SMTP_PORT (default 587), SMTP_USER, SMTP_PASS, EMAIL_FROM (optional)
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
import smtplib
import sys
from dataclasses import dataclass
from email.message import EmailMessage
from pathlib import Path
from typing import Iterable


DEFAULT_UNAVAILABLE_PATTERNS = [
    r"no\s+appointments?\s+available",
    r"currently\s+no\s+appointments?",
    r"there\s+are\s+no\s+available\s+appointments?",
    r"earliest\s+appointment\s+is\s+not\s+available",
]

DEFAULT_AVAILABLE_PATTERNS = [
    r"available\s+appointment",
    r"earliest\s+appointment",
    r"select\s+date",
    r"schedule\s+appointment",
    r"book\s+appointment",
]

DEFAULT_CDP_URLS = ",".join(
    [
        "http://127.0.0.1:9222",
        "http://localhost:9222",
        "http://127.0.0.1:9223",
        "http://localhost:9223",
    ]
)


@dataclass
class CheckResult:
    checked_at_utc: str
    status: str
    details: str
    url: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check US visa appointment availability.")
    parser.add_argument(
        "--status",
        choices=["available", "unavailable", "unknown"],
        help="Manual status override if you already know the result.",
    )
    parser.add_argument(
        "--details",
        default="",
        help="Optional details to include in logs and emails.",
    )
    parser.add_argument(
        "--check-live",
        action="store_true",
        help="Deprecated: live checking is now default behavior.",
    )
    parser.add_argument(
        "--no-live-check",
        action="store_true",
        help="Skip live Chrome CDP check (not recommended for automation runs).",
    )
    parser.add_argument(
        "--cdp-url",
        default=os.getenv("CHROME_CDP_URL", DEFAULT_CDP_URLS),
        help="Comma-separated Chrome DevTools URLs (default tries common localhost ports).",
    )
    parser.add_argument(
        "--page-url-contains",
        default=os.getenv("VISA_PAGE_URL_CONTAINS", "ais.usvisa-info.com"),
        help="Find an open tab whose URL contains this value.",
    )
    parser.add_argument(
        "--log-file",
        default="automations/visa-appoitnment-scheduler/availability_log.csv",
        help="CSV file for per-run logging.",
    )
    parser.add_argument(
        "--notify-email",
        default="borabalabanli@gmail.com",
        help="Email target for availability alerts.",
    )
    parser.add_argument(
        "--timezone",
        default=os.getenv("TZ", "Europe/Istanbul"),
        help="Timezone label used in email body.",
    )
    return parser.parse_args()


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def has_any_pattern(text: str, patterns: Iterable[str]) -> bool:
    return any(re.search(pattern, text, flags=re.IGNORECASE) for pattern in patterns)


def infer_status_from_text(text: str) -> tuple[str, str]:
    normalized = normalize_text(text)

    if has_any_pattern(normalized, DEFAULT_UNAVAILABLE_PATTERNS):
        return "unavailable", "Matched known unavailable patterns on the page"

    if has_any_pattern(normalized, DEFAULT_AVAILABLE_PATTERNS):
        return "available", "Matched known available patterns on the page"

    return "unknown", "Could not match available/unavailable patterns"


def parse_cdp_urls(cdp_url_value: str) -> list[str]:
    urls = [url.strip() for url in cdp_url_value.split(",") if url.strip()]
    return urls or ["http://127.0.0.1:9222"]


def check_live_page(cdp_url: str, page_url_contains: str) -> tuple[str, str, str]:
    try:
        from playwright.sync_api import sync_playwright  # type: ignore
    except Exception as exc:  # pragma: no cover
        return "unknown", f"Playwright import failed: {exc}", ""

    cdp_urls = parse_cdp_urls(cdp_url)
    errors: list[str] = []
    no_match_endpoints: list[str] = []

    for current_cdp_url in cdp_urls:
        try:
            with sync_playwright() as p:
                browser = p.chromium.connect_over_cdp(current_cdp_url)
                for context in browser.contexts:
                    for page in context.pages:
                        page_url = page.url or ""
                        if page_url_contains.lower() in page_url.lower():
                            text = page.content()
                            status, details = infer_status_from_text(text)
                            return status, details, page_url

                no_match_endpoints.append(current_cdp_url)
                continue
        except Exception as exc:  # pragma: no cover
            errors.append(f"{current_cdp_url}: {exc}")

    if no_match_endpoints:
        return (
            "unknown",
            "No open tab matched URL pattern "
            f"'{page_url_contains}' on endpoints: {', '.join(no_match_endpoints)}",
            "",
        )

    return "unknown", f"Live check failed via CDP. Tried: {' | '.join(errors)}", ""


def append_log(log_file: Path, result: CheckResult) -> None:
    log_file.parent.mkdir(parents=True, exist_ok=True)
    file_exists = log_file.exists()

    with log_file.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["checked_at_utc", "status", "details", "url"],
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(
            {
                "checked_at_utc": result.checked_at_utc,
                "status": result.status,
                "details": " ".join(result.details.split()),
                "url": " ".join(result.url.split()),
            }
        )


def send_email_if_available(result: CheckResult, recipient: str, tz_label: str) -> tuple[bool, str]:
    if result.status != "available":
        return False, "Status is not available; email not sent"

    host = os.getenv("SMTP_HOST")
    port = int(os.getenv("SMTP_PORT", "587"))
    username = os.getenv("SMTP_USER")
    password = os.getenv("SMTP_PASS")
    sender = os.getenv("EMAIL_FROM") or username

    missing = [
        key
        for key, value in {
            "SMTP_HOST": host,
            "SMTP_USER": username,
            "SMTP_PASS": password,
            "EMAIL_FROM or SMTP_USER": sender,
        }.items()
        if not value
    ]
    if missing:
        return False, f"Missing email configuration: {', '.join(missing)}"

    msg = EmailMessage()
    msg["Subject"] = "US Visa Appointment Availability Detected"
    msg["From"] = sender
    msg["To"] = recipient
    msg.set_content(
        "\n".join(
            [
                "Appointment availability appears to be OPEN.",
                f"Checked at (UTC): {result.checked_at_utc}",
                f"Timezone label: {tz_label}",
                f"Page URL: {result.url or 'N/A'}",
                f"Detection details: {result.details}",
            ]
        )
    )

    try:
        with smtplib.SMTP(host, port, timeout=30) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
        return True, f"Alert email sent to {recipient}"
    except Exception as exc:  # pragma: no cover
        return False, f"Failed to send email: {exc}"


def main() -> int:
    args = parse_args()

    now_utc = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

    status = args.status
    details = args.details.strip()
    url = ""

    # Always run a live check per invocation unless explicitly disabled.
    if not args.no_live_check:
        live_status, live_details, url = check_live_page(args.cdp_url, args.page_url_contains)
        status = live_status
        details = details or live_details
        # Allow manual override only when live status could not be determined.
        if args.status and live_status == "unknown":
            status = args.status
            details = details or "Manual override used because live check returned unknown"

    if not status:
        status = "unknown"
        details = details or "No status provided and live check disabled"

    result = CheckResult(
        checked_at_utc=now_utc,
        status=status,
        details=details,
        url=url,
    )

    append_log(Path(args.log_file), result)
    email_sent, email_note = send_email_if_available(result, args.notify_email, args.timezone)

    print(f"checked_at_utc={result.checked_at_utc}")
    print(f"status={result.status}")
    print(f"details={result.details}")
    print(f"url={result.url or 'N/A'}")
    print(f"email={email_note}")
    return 0 if status in {"available", "unavailable", "unknown"} else 1


if __name__ == "__main__":
    sys.exit(main())
