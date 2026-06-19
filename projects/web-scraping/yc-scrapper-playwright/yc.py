import asyncio
from playwright.async_api import async_playwright
import csv

url = "https://www.ycombinator.com/companies"


async def scrape_yc():
    async with async_playwright() as pw:
        chromium = await pw.chromium.launch(headless=True)
        page = await chromium.new_page()

        await page.goto(url)
        await page.wait_for_selector("a[href*='/companies/']", timeout=10000)

        cards = await page.locator("a[href*='/companies/']").all()

        names, links, descriptions, batches = [], [], [], []

        for card in cards[:20]:
            name = await card.locator("span").nth(0).inner_text()
            desc_el = card.locator("div.mb-1\\.5 span")
            desc = await desc_el.inner_text() if await desc_el.count() else ""
            link = await card.get_attribute("href")
            batch = await card.locator("span.pill").first.inner_text()

            names.append(name.strip())
            links.append(link)
            descriptions.append(desc.strip())
            batches.append(batch.strip())

        await chromium.close()
        return names, links, descriptions, batches


names, links, descriptions, batches = asyncio.run(scrape_yc())

with open("yc.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Link", "Description", "Batch"])

    for name, link, desc, batch in zip(names, links, descriptions, batches):
        writer.writerow([name, link, desc, batch])
