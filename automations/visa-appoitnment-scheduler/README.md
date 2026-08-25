# Visa Appointment Scheduler

This checker logs every run and sends an email only when appointment status is detected as `available`.

## Run

```powershell
python automations/visa-appoitnment-scheduler/check_appointment.py
```

## What it does each run

- Checks status from the open Chrome visa tab via CDP (default on every run)
- Appends a row to `automations/visa-appoitnment-scheduler/availability_log.csv`
- Sends email to `borabalabanli@gmail.com` if status is `available`

## Chrome requirement for live check

The script reads your already-open US visa page from Chrome through CDP. Start Chrome with remote debugging enabled:

```powershell
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

Then keep the visa appointment tab open (`ais.usvisa-info.com`) and run the script.
Use `--no-live-check` only if you intentionally want to skip live checking.

You can provide multiple CDP endpoints in one run, for example:

```powershell
python automations/visa-appoitnment-scheduler/check_appointment.py --cdp-url "http://127.0.0.1:9222,http://localhost:9222"
```

## Email config (env vars)

- `SMTP_HOST`
- `SMTP_PORT` (optional, default `587`)
- `SMTP_USER`
- `SMTP_PASS`
- `EMAIL_FROM` (optional; defaults to `SMTP_USER`)

## Manual status mode

```powershell
python automations/visa-appoitnment-scheduler/check_appointment.py --status unavailable --details "No slots shown"
```

