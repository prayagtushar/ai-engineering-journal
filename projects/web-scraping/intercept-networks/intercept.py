import asyncio
from playwright.async_api import async_playwright
import json


async def intercept_yc():
    captured = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        # Register a listener BEFORE navigating
        # It fires for every network response the page receives
        async def handle_response(response):
            url = response.url
            # Filter for responses that look like data APIs
            if "algolia" in url or "/api/" in url or "companies" in url:
                try:
                    data = await response.json()
                    captured.append({"url": url, "data": data})
                    print(f"Captured: {url}")
                except Exception:
                    pass  # not JSON, skip it

        page.on("response", handle_response)

        await page.goto("https://www.ycombinator.com/companies")
        await page.wait_for_load_state("networkidle")

        await browser.close()

    return captured


results = asyncio.run(intercept_yc())

if results:
    print(f"\nCaptured {len(results)} API responses")
    # Print the first one pretty
    print(json.dumps(results[0]["data"], indent=2)[:3000])
else:
    print("No API responses captured")
