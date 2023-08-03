import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.livechart.me/"

# response = requests.get(url)
# chome optins
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless=new')


response = webdriver.Chrome(options=options)
response.get(url)
soup = BeautifulSoup(response.page_source, "html.parser")
# soup = BeautifulSoup(response.text, "html.parser")
with open ("livechart.html","w", encoding="utf-8") as f:
    f.write(soup.prettify())
    
print(soup.prettify())