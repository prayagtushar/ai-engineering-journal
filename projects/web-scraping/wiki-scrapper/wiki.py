import wikipediaapi
import csv

wiki = wikipediaapi.Wikipedia(language="en", user_agent="web-scrapping-project")

company = str(input("Enter the company name? "))
page = wiki.page(company)


if not page.exists():
    print("Page not found")
    exit()

print(page.title)
print(page.fullurl)

with open("company-details.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Section", "Text"])
    for section in page.sections:
        writer.writerow([section.title, section.text])
