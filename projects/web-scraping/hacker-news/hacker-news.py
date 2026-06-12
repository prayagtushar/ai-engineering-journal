import requests

url = "https://hacker-news.firebaseio.com/v0"

top_ids = requests.get(f"{url}/topstories.json").json()
print(f"Total top story IDs: {len(top_ids)}")
print(f"First 5 IDs: {top_ids[:5]}")

stories = []
for story_id in top_ids[:20]:
    item = requests.get(f"{url}/item/{story_id}.json").json()
    stories.append(
        {
            "id": item.get("id"),
            "title": item.get("title"),
            "url": item.get("url", ""),
            "score": item.get("score"),
            "by": item.get("by"),
            "time": item.get("time"),
            "descendants": item.get("descendants", 0),
        }
    )


for s in stories[:5]:
    print(s)
    
    
# /topstories.json	List of top story IDs (up to 500)
# /newstories.json	Newest stories
# /beststories.json	Best stories
