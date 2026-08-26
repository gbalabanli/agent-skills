---
name: get-screenshot
description: Capture screenshots of web pages using Playwright. Use when the user asks to screenshot a page, capture a webpage, take a snapshot of a URL, save a page as an image, or needs visual evidence of a web page's appearance.
---

# Get Screenshot

## Overview

Capture screenshots of web pages using a Playwright-based CLI tool. Supports custom viewports, full-page capture, and output to any path.

## Tool Location

```
C:\Users\Bora\Desktop\Workspace\agents\agent-tools\
```

## Usage

### Basic screenshot

```bash
uv run get-screenshots <url> -o <output_path>
```

### With options

```bash
uv run get-screenshots <url> -o <output_path> --width 1920 --height 1080 --full-page
```

## Options

| Flag | Description | Default |
|------|-------------|---------|
| `url` | URL to capture (positional, required) | — |
| `-o, --output` | Output file path | `screenshot.png` |
| `--width` | Viewport width in pixels | `1280` |
| `--height` | Viewport height in pixels | `720` |
| `--full-page` | Capture full scrollable page | `false` |

## Workflow

### 1) Determine the target

- Extract the URL from the user's request.
- If the user provides HTML content instead of a URL, save it to a temporary file and use a `file://` path.

### 2) Set output path

- Default to `screenshot.png` in the current directory unless the user specifies otherwise.
- Use descriptive filenames when capturing multiple pages (e.g., `homepage.png`, `login-page.png`).

### 3) Choose viewport

- Use default 1280x720 unless the user specifies dimensions.
- For mobile screenshots, suggest `--width 375 --height 812` (iPhone X).
- For full-page captures, add `--full-page`.

### 4) Execute

```bash
uv run get-screenshots https://example.com -o screenshot.png
```

Run from the tool directory:

```bash
uv run get-screenshots https://example.com -o screenshot.png
```

**Important:** The command must be run from the `agent-tools` project directory where `pyproject.toml` is located. Use the `workdir` parameter in bash:

```bash
# Correct
uv run get-screenshots https://example.com -o output.png
# with workdir set to: C:\Users\Bora\Desktop\Workspace\agents\agent-tools
```

### 5) Verify output

- Confirm the file was created and has non-zero size.
- Report the file path and size to the user.

## Examples

**Capture a page at default viewport:**
```bash
uv run get-screenshots https://example.com -o example.png
```

**Capture at mobile resolution:**
```bash
uv run get-screenshots https://example.com -o mobile.png --width 375 --height 812
```

**Capture full scrollable page:**
```bash
uv run get-screenshots https://example.com -o full-page.png --full-page
```

**Capture at 4K resolution:**
```bash
uv run get-screenshots https://example.com -o 4k.png --width 3840 --height 2160
```

## Prerequisites

- Python 3.11+
- uv package manager
- Playwright Chromium installed (`uv run playwright install chromium`)

## Error Handling

- If the URL is unreachable, the tool will raise a Playwright navigation error. Report this to the user and suggest checking the URL.
- If the output path is invalid, check directory permissions.
- If Playwright is not installed, run `uv run playwright install chromium` first.
