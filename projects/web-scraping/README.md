# Web Scraping — Learning Guide

A hands-on guide to web scraping in Python, from simple to advanced.
Type each file out yourself to learn. Don't copy-paste.

## Setup

```bash
pip install requests beautifulsoup4 playwright httpx pandas
playwright install chromium
```

## Files — Do These in Order

| File | Approach | When to Use |
|------|----------|-------------|
| `01_requests_bs4.py` | requests + BeautifulSoup | Static HTML pages |
| `02_pagination.py` | Pagination | Multi-page sites |
| `03_api.py` | Official API | When a site exposes an API |
| `04_playwright.py` | Headless browser | JavaScript-rendered pages (SPAs) |
| `05_intercept_network.py` | Network interception | Capture hidden API calls |
| `06_build_dataset.py` | Full pipeline | Save everything to CSV/JSON |

## Decision Tree — Which Approach to Use?

```
Does the site have an official API?
  YES → Use the API (03_api.py)
  NO ↓

Does the page load content without JavaScript?
  (Test: requests.get() — is the data in response.text?)
  YES → requests + BeautifulSoup (01 / 02)
  NO ↓

Does the page make XHR/fetch API calls you can intercept?
  (DevTools → Network → XHR tab while loading)
  YES → Intercept network requests (05_intercept_network.py)
  NO ↓

Use Playwright to render the page (04_playwright.py)
```

## Key DevTools Skills

The most important skill in scraping is reading your browser's DevTools:

- **Elements tab** — right-click any element → Inspect → find the CSS selector
- **Network tab** — filter by XHR/Fetch to see what API calls a page makes
- **Copy selector** — right-click an element in Elements → Copy → Copy selector

## Ethics & Rules

- Always check `robots.txt` before scraping (`https://site.com/robots.txt`)
- Add `time.sleep(1)` between requests — don't hammer servers
- Prefer official APIs over scraping when available
- Don't scrape personal data without a clear purpose
- Don't bypass login walls or CAPTCHAs

## Suggested Learning Path

1. **Day 1** — `01_requests_bs4.py` — scrape HN headlines, understand HTML parsing
2. **Day 2** — `02_pagination.py` — loop through pages, build a list
3. **Day 3** — `03_api.py` — use HN's official API, compare with Day 1 output
4. **Day 4** — `04_playwright.py` — install Playwright, watch it run headless
5. **Day 5** — `05_intercept_network.py` — open DevTools, find hidden API calls
6. **Day 6** — `06_build_dataset.py` — combine everything, export a real dataset
