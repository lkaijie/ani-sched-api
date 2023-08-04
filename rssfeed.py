import datetime
import requests
import feedparser
import json
import time


# track time taken to run the script
start_time = time.time()


recently_aired ="https://www.livechart.me/feeds/episodes"  # for recently aired episodes
headlines = "https://www.livechart.me/feeds/headlines" # for news headlines


# response = requests.get(recently_aired)
# feed = feedparser.parse(recently_aired)


# TESTS ONLY IGNORE
current_time = datetime.datetime.now(datetime.timezone.utc)
# Calculate the date 24 hours ago
previous_day = current_time - datetime.timedelta(hours=24)

# Format the previous day's date in the required format
if_modified_since_date = previous_day.strftime('%a, %d %b %Y %H:%M:%S GMT')
headers = {
    'If-Modified-Since': if_modified_since_date
}

wrong_headers = {
    'If-Modified-Since': "jwhefiohew"
}
# no more ignore

feed = feedparser.parse(recently_aired)
# entries contain all the news headlines
entries = feed.entries
def tests():
    # print(entries)
    # print(entries[0].title)
    print("type of entries: ",type(entries))
    print(entries[0].keys())
    print(entries[0])
# tests()

json_object = json.dumps(entries, indent = 4)
with open("rssfeed[recently_aired].json","w", encoding="utf-8") as f:
    f.write(json_object)
    
end_time = time.time()

print("Time taken to run the script: ", end_time - start_time)