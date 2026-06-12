import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://news.ycombinator.com/newest?p={page}"

pages = int(input("Enter how many stories you want to fetch?"))

news_list = []
scores_list = []

for news in range(1, pages):
    response = requests.get(url.format(page=pages), headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.select(".athing"):
        subrow = item.find_next_sibling("tr")

        title = item.select(".titleline > a")
        score = subrow.select(".score") if subrow else []
        author = subrow.select(".hnuser") if subrow else []

        if title and score:
            news_list.append({"title": title[0].text, "url": title[0]["href"]})
            scores_list.append({"scores": score[0].text, "author": author[0].text if author else "N/A"})

    time.sleep(1)


with open("yc_paginated.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "URL", "Score", "Author"])

    for news, score in zip(news_list, scores_list):
        writer.writerow([news["title"], news["url"], score["scores"], score["author"]])
