import wikipediaapi

# Any company with Wikipedia Article can be captured here
wiki = wikipediaapi.Wikipedia(user_agent="your_name/information", language="en")

page = wiki.page("Groww")
text = page.text
summary = page.summary
links = page.links
