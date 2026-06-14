import asyncio
from playwright.async_api import async_playwright
import json


USEFUL_FIELDS = [
    "name",
    "slug",
    "one_liner",
    "long_description",
    "batch",
    "website",
    "tags",
    "status",
]


def extract_companies(raw):
    hits = raw.get("results", [{}])[0].get("hits", [])
    extracted = [{k: hit[k] for k in USEFUL_FIELDS if k in hit} for hit in hits]
    return [c for c in extracted if c.get("name")]


async def intercept_yc():
    captured = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        async def handle_response(response):
            url = response.url
            if "algolia.net" in url and "/queries" in url:
                try:
                    data = await response.json()
                    captured.append({"url": url, "data": data})
                except Exception:
                    pass

        page.on("response", handle_response)

        url = "https://www.ycombinator.com/companies"

        await page.goto(url)
        await page.wait_for_load_state("networkidle")

        await browser.close()

    return captured


results = asyncio.run(intercept_yc())

companies = []
for r in results:
    companies.extend(extract_companies(r["data"]))

if companies:
    print(f"Captured {len(companies)} companies")
    with open("captured_apis.json", "w", encoding="utf-8") as f:
        json.dump(companies, f, indent=2)
    print("Saved to captured_apis.json")
else:
    print("No API responses captured")
