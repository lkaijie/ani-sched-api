import requests
import feedparser
import json


recently_aired ="https://www.livechart.me/feeds/episodes"  # for recently aired episodes
headlines = "https://www.livechart.me/feeds/headlines" # for news headlines


# response = requests.get(recently_aired)
# feed = feedparser.parse(recently_aired)
feed = feedparser.parse(headlines)
# print(feed)
entries = feed.entries

# print(entries)
# print(entries[0].title)
print("type of entries: ",type(entries))
print(entries[0].keys())
print(entries[0])
# put the first entry into a json file


json_object = json.dumps(entries[0], indent = 4)
print(json_object)
with open("livechart.json","a", encoding="utf-8") as f:
    f.write(json_object)
    
