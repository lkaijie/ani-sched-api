import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the root directory by going up one level from the script directory
root_dir = os.path.dirname(script_dir)

# Append the root directory to the Python path
sys.path.append(root_dir)
# print(sys.path)
from ani_sched import *

ani_sched = AniSched()

def test_get_sched():
    # url = "https://www.livechart.me/fall-2022/tv?titles=english"    
    result = ani_sched.get_sched(year=2022, season="fall")
    assert result != None
    subject = result["BOCCHI THE ROCK!"]
    assert subject["title"] == "BOCCHI THE ROCK!"
    assert subject["tags"] == ['CGDCT', 'Comedy', 'Music']
    assert subject["img_url"] == "https://u.livechart.me/anime/10424/poster_image/505b08d622b214e39f4744f65794a124.webp/small.jpg"
    # assert subject["rating"] == "8.69 " # maybe not use this it might change?
    assert subject["studio"] == ['CloverWorks']
    # assert subject["date"] == "Oct 8, 2022 at 9:00am MDT"
    assert subject["source"] == "4-koma Manga"
    assert subject["episodes"] == "12 eps × 24m"

def test_get_news():
    items = ani_sched.get_news()
    print(f"HEADLINES: {items}")
    assert items != None

def test_get_recently_aired():
    items = ani_sched.get_recently_aired()
    print(f"RECENTLY_AIRED: {items}")
    assert items != None
    
def test_search():
    items = ani_sched.search_anime("bocchi")
    print(f"SEARCH: {items}")
    assert items != None
    assert items[0][0] == "BOCCHI THE ROCK!"
    assert items[0][1] == "https://www.livechart.me/anime/10424"

def test_extract_link():
    link_to_extract = "https://www.livechart.me/anime/10424"
    subject = ani_sched.extract_link(link_to_extract)

    assert subject != None
    # subject = result["BOCCHI THE ROCK!"]
    assert subject["title"] == "BOCCHI THE ROCK!"
    assert subject["tags"] == ['CGDCT', 'Comedy', 'Music']
    assert subject["img_url"] == "https://u.livechart.me/anime/10424/poster_image/505b08d622b214e39f4744f65794a124.webp/small.jpg"
    # assert subject["rating"] == "8.69 " # maybe not use this it might change?
    assert subject["studio"] == ['CloverWorks']
    # assert subject["date"] == "Oct 8, 2022 at 9:00am MDT"
    assert subject["source"] == "4-koma Manga"
    # assert subject["episodes"] == "12 eps × 24m"
    