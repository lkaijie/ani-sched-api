import requests
from bs4 import BeautifulSoup



# url = "https://anichart.net/Summer-2023"
# url = "https://animeschedule.net/seasons/upcoming"
url = "https://myanimelist.net/anime/season"


response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
        
sections = soup.find('div',class_="js-categories-seasonal")
for section in sections.find_all('div'):
    try:
        print(section.find('div',class_="anime-header").text+" animes \n")
        for anime in section.find_all('h2',class_="h2_anime_title"):
            print(anime.text)
        print("\n")
    except:
        pass    
print("done")