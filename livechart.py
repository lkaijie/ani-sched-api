import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
url = "https://www.livechart.me/"

# response = requests.get(url)
# chome optins
start_time = time.time()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless=new')


response = webdriver.Chrome(options=options)
response.get(url)
soup = BeautifulSoup(response.page_source, "html.parser")
# soup = BeautifulSoup(response.text, "html.parser")

animes = {}

for x in soup.find_all("div", class_="anime-card"):
    title = x.find("a", attrs={"data-anime-card-target":"mainTitle"}).text
    tags = []
    for y in x.find_all("ol", class_="anime-tags"):
        for a in y.find_all("a"):
            tags.append(a.text)      
    img_url = x.find("img", attrs={"data-anime-card-target":"poster"})["src"]
    try:
        rating = x.find("div", class_="anime-avg-user-rating").text
    except:
        rating = "Unknown"
    studio = []
    for y in x.find_all("ul", class_="anime-studios"):
        for a in y.find_all("a"):
            studio.append(a.text)
    date = x.find("div", class_="anime-date").text
    for y in x.find("div", class_="anime-metadata"):
        try:
            source = y.find("div", class_="anime-source").text
            episodes = y.find("div", class_="anime-episodes").text
        except:
            source = "Unknown"
            episodes = "Unknown"
    summary = x.find("div", class_="anime-synopsis").text
    # remove or add note section
    links = []
    for y in x.find_all("ul", class_="related-links"):
        for a in y.find_all("a"):
            links.append(a["href"])
            
    info = {
        "title": title,
        "tags": tags,
        "img_url": img_url,
        "rating": rating,
        "studio": studio,
        "date": date,
        "source": source,
        "episodes": episodes,
        "summary": summary,
        "links": links
    }
    animes[title] = info
        
    
    
        # tags = [
        #     a.text for a in x.find_all("a")
        # ]
    
    # tags = [
    #     a.text for x in soup.find_all("ol", class_="anime-tags")
    #         for a in x.find_all("a")
    # ]
    # print(tags)
    


# with open ("livechart.html","w", encoding="utf-8") as f:
#     # f.write(soup.prettify())
#     f.write(str(soup.find_all("div", class_="anime-card")))
    
# print(soup.prettify())
print(animes)
end_time = time.time()
print("Time taken to run the script: ", end_time - start_time)