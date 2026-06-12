import requests
from bs4 import BeautifulSoup
import csv

url = "https://news.ycombinator.com/news"

res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

print(f"Status: {res.status_code}")

soup = BeautifulSoup(res.text, "html.parser")

news_list = soup.select(".titleline > a")
news_score = soup.select(".subline > span")

print(f"Found {len(news_list)} stories")

with open("yc_stories.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Title", "Url", "Score"])

    for news, score in zip(news_list, news_score):
        writer.writerow([news.text, news["href"], score.text])
    
print("YC NEWS STORIES SAVED in yc_stories.csv")
