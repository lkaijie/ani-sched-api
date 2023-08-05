import feedparser
import json
import requests
from selenium import webdriver
from bs4 import BeautifulSoup



class _Base:
    def __init__(self, timeout: int) -> None:
        self.timeout = timeout
        
    def _parse_url(self, url: str, type: str = None) -> None:
        """Returns a BeautifulSoup object of the url

        Args:
            url (str): Url to parse
            type (str, optional): "selenium" allows for browsers that require JS, leave empty for requests instead. Defaults to None.

        Returns:
            soup: BeautifulSoup object of the url
        """
        if type == "normal" or type == None:
            # use requests
            response = requests.get(url, timeout=self.timeout)
            soup = BeautifulSoup(response.text, "html.parser", from_encoding="utf-8")
            return soup
        
        elif type == "selenium":
            # use selenium
            options = webdriver.ChromeOptions()
            options.add_argument('--ignore-certificate-errors')
            options.add_argument('--headless=new')    
            response = webdriver.Chrome(options=options)
            response.get(url)
            soup = BeautifulSoup(response.page_source, "html.parser", from_encoding="utf-8")
            return soup
        
    
    def _parse_feed(self, url: str) -> None:
        """Returns a list of dicts containing the entries of the feed

        Args:
            url (str): url of rss feed
        """
        feed = feedparser.parse(url)
        entries = feed.entries
        return entries
        
    def _get_redirect(self, url: str) -> str:
        """Returns the redirected url

        Args:
            url (str): url to redirect

        Returns:
            str: redirected url
        """
        response = requests.get(url, timeout=self.timeout)
        return response.url
    
    