import requests
from bs4 import BeautifulSoup



# url = "https://anichart.net/Summer-2023"
# url = "https://animeschedule.net/seasons/upcomi ng"
# url = "https://myanimelist.net/anime/season"
url = "https://www.livechart.me/"


# response = requests.get(url)
# print(response.url)
# soup = BeautifulSoup(response.text, "html.parser")
        
# sections = soup.find('div',class_="js-categories-seasonal")
# for section in sections.find_all('div'):
#     try:
#         print(section.find('div',class_="anime-header").text+" animes \n")
#         for anime in section.find_all('h2',class_="h2_anime_title"):
#             print(anime.text)
#         print("\n")
#     except:
#         pass    
# print("done")

import datetime

def get_current_season():
    current_month = datetime.datetime.now().month
    current_year = datetime.datetime.now().year
    
    if 1 <= current_month <= 3:
        return f"winter-{current_year}"
    elif 4 <= current_month <= 6:
        return f"spring-{current_year}"
    elif 7 <= current_month <= 9:
        return f"summer-{current_year}"
    elif 10 <= current_month <= 12:
        return f"fall-{current_year}"
    else:
        return "Unknown"
url = "https://www.livechart.me/"

current = get_current_season()

url = url+current+"/tv?titles=english"
# print(get_current_season())
print(url)