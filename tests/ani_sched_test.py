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


def test_get_news():
    items = ani_sched.get_news()
    print(f"HEADLINES: {items}")
    
    assert items != None

def test_get_recently_aired():
    items = ani_sched.get_recently_aired()
    print(f"RECENTLY_AIRED: {items}")
    
    assert items != None
    
def test_get_sched():
    fall_2022 = ani_sched.get_sched(year=2022,season="fall")
    dummy = fall_2022["TV (New)"][6]
    
    assert dummy != None
    assert dummy["title"] == "Bocchi the Rock!"
    # assert dummy["rating"] == "8.83"
    assert dummy["studio"] == ["CloverWorks"]
    assert dummy["link"] == "https://myanimelist.net/anime/47917/Bocchi_the_Rock"
    
def test_search_anime():
    anime = ani_sched.search_anime("bocchi the rocks")
    
    assert anime[0][0] == "Bocchi the Rock!"
    assert anime[0][1] == "https://myanimelist.net/anime/47917/Bocchi_the_Rock"
    
def test_extract_seach_link():
    url = "https://myanimelist.net/anime/47917/Bocchi_the_Rock"
    anime = ani_sched.extract_search_link(url=url)
    
    assert anime != None
    assert anime["title"] == "Bocchi the Rock!"
    # assert anime["rating"] == "8.83"
    assert anime["studio"] == "CloverWorks"
    assert anime["link"] == "https://myanimelist.net/anime/47917/Bocchi_the_Rock"
    