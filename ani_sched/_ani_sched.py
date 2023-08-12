import datetime
from ani_sched import _base
from ani_sched._base import _Base
import ani_sched.config as config
from typing import List, Dict
import re

class AniSched(_Base):
    """AniSched class, used to get anime schedules from MyAnimeList

    Methods:
        get_sched(season=None, year=None)
        
        get_news()
        
        get_recently_aired()
    Args:
        timeout (int, optional): Timeout for the requests. Defaults to config.TIMEOUT.
    """
    def __init__(self, timeout: int = config.TIMEOUT) -> None:
        super().__init__(timeout)
        self.headline_url = config.HEADLINE_ENDPOINT
        self.recently_aired_url = config.RECENTLY_AIRED_ENDPOINT

        self.mal_url = config.MAL_SCHEDULE_ENDPOINT
        self.search_url = config.MAL_SEARCH_ENDPOINT


    def get_sched(self, season=None, year=None)-> Dict[str, List[Dict]]:
        """Extracts and returns the schedule from MyAnimeList

        Args:
            season (str, optional): season of anime. Defaults to None.
            year (int, optional): year of season. Defaults to None.

        Returns:
            Dict[str, List[Dict]]: Dict of lists of dicts containing the schedule
            
        Example:
            {"TV (New)": [{"title": "Bocchi the Rock!",...}]}
        """

        def _extract_schedule(soup) -> List[Dict]:
            """Extracts the schedule from the soup object

            Args:
                soup (BeautifulSoup4 Object): BeautifulSoup4 object of the schedule page ex. https://myanimelist.net/anime/season

            Returns:
                list: List of dicts containing animes in the schedule
            """
            animes = {}
            
            def extract_anime_type(soup):
                animes = []
                # js-anime-category-producer seasonal-anime
                for x in soup.find_all("div", class_=re.compile(r'\bjs-anime-category-producer\b.*\bseasonal-anime\b')):
                    title = x.find("a", class_="link-title").text
                    try:
                        title_eng = x.find("a", class_="link-title-english").text
                    except:
                        title_eng = title
                    rating = x.find("div", attrs={"title":"Score"}).text.replace("\n", "").strip()
                    try:
                        img_url = x.find("img")["data-src"]
                    except:
                        img_url = x.find("img")["src"]

                    members = x.find("div", attrs={"title":"Members"}).text.replace("\n", "").strip()
                    tags = []
                    for y in x.find_all("span", class_ = "genre"):
                        tags.append(y.text.replace("\n", ""))
                    studio = []
                    properties = x.find("div", class_ = "properties")
                    properties = properties.find_all("div")
                    for u in properties[0].find_all("span", class_ = "item"):
                        studio.append(u.text)
                    source = properties[1].find("span", class_ = "item").text
                    summary = x.find("p", class_ = "preline").text.replace("\n", "").replace("\r", "").strip()
                    link = x.find("a", class_ = "link-title")["href"]
                    date_and_episode = x.find("div", class_ = "prodsrc")
                    date_and_episode = date_and_episode.find("div",class_="info")
                    date_and_episode = date_and_episode.find_all("span", class_="item")
                    start_date = date_and_episode[0].text.replace("\n", "").strip()
                    episodes = date_and_episode[1].text.replace("\n", "").replace("         ", "").strip()
                    
                    anime_info = {
                        "title": title,
                        "title_eng": title_eng,
                        "rating": rating,
                        "img_url": img_url,
                        "members": members,
                        "tags": tags,
                        "studio": studio,
                        "source": source,
                        "summary": summary,
                        "episodes": episodes,
                        "start_date": start_date,
                        "link": link
                    }
                    animes.append(anime_info)
                return animes
            
            new_soup = soup.find("div", class_="js-categories-seasonal")
            for type_of_anime in new_soup.find_all("div", class_=re.compile(r'\bseasonal-anime-list\b.*\bjs-seasonal-anime-list\b')):
                anime_type = type_of_anime.find("div", class_="anime-header").text
                match anime_type:
                    case "TV (New)":
                        animes["TV (New)"] = extract_anime_type(type_of_anime)
                        continue
                    case "TV (Continuing)":
                        animes["TV (Continuing)"] = extract_anime_type(type_of_anime)
                        continue
                    case "ONA":
                        animes["ONA"] = extract_anime_type(type_of_anime)
                        continue
                    case "OVA":
                        animes["OVA"] = extract_anime_type(type_of_anime)
                        continue
                    case "Movie":
                        animes["Movie"] = extract_anime_type(type_of_anime)
                        continue
                    case "Special":
                        animes["Special"] = extract_anime_type(type_of_anime)
                        continue
                    case _:
                        continue
            return animes
   
        if not season: # if no season is provided, get the current season
            entries = self._parse_url(self.mal_url)
            return _extract_schedule(entries)
        else:
            if not season and not year:
                raise ValueError("Must provide season and year")
            elif season not in ["winter", "spring", "summer", "fall"]:
                raise ValueError("Season must be one of the following: winter, spring, summer, fall")
            else:
                endpoint = f"{self.mal_url}/{year}/{season}"
                return _extract_schedule(self._parse_url(endpoint))
                
    def get_news(self) -> None:
        """Returns a list of dicts containing the news entries of the feed
        """
        entries = self._parse_feed(self.headline_url)
        return entries
    
    def get_recently_aired(self) -> None:
        """Returns a list of dicts containing the recently aired anime
        """
        entries = self._parse_feed(self.recently_aired_url)
        return entries
        
    def search_anime(self, query:str) -> List:
        """Returns a list of the first 5 search results

        Args:
            query (str): The search query

        Returns:
            List: returns a list in the format of [title, url]
        """
        # MAL_SEARCH_ENDPOINT = 'https://myanimelist.net/search/all'
        query = query.replace(" ", "%20")
        category = "all"
        url = f"{self.search_url}?cat={category}&q={query}"
        entries = self._parse_url(url)
        
        results = entries.find_all("div", class_="list di-t w100")
        search_results = []
        for x in results[:5]:
            title = x.find("a", class_="hoverinfo_trigger fw-b fl-l").text
            url = x.find("a", class_="hoverinfo_trigger fw-b fl-l")["href"]
            print(title, url)
            # search_results.append([title, url])
        return search_results
   
    def extract_search_link()
        
    # # def extract_link(self, url: str) -> Dict:
    #     """Returns a dict containing the anime info

    #     Args:
    #         url (str): The url of the anime

    #     Returns:
    #         dict: returns a dict containing the anime info
    #     """
    #     # title, tags, img_url, rating, studio, date, source, episodes, summary, links
    #     entries = self._parse_url(url, type="selenium")
    #     title = entries.find("span", class_="text-base-content").text
    #     tags = []
    #     for x in entries.find_all("a", class_="lc-chip-button", attrs={"data-anime-details-target":"tagChip"}):
    #         tags.append(x.text)
    #     img_url = entries.find("img", class_="overflow-hidden rounded w-24 xs:w-40")["src"]
    #     rating = entries.find("span", class_="text-lg font-bold").text
    #     studio = []
    #     x = entries.find("div", class_="flex flex-wrap gap-2")
    #     for a in x.find_all("a"):
    #         studio.append(a.text)
            
    #     # studio = entries.find("a", class_="lc-chip-button").text
    #     source = entries.find("div", class_="whitespace-nowrap text-ellipsis overflow-hidden").text
    #     try:
    #         episodes = entries.find("div", attrs={"data-action":"click->anime-details#openListEditor"}).text
    #     except:
    #         episodes = "Unknown"
    #     summary = entries.find("div", class_="lc-expander-content lc-markdown-html cursor-pointer select-none").text
    #     links = []
    #     x = entries.find_all("div", class_="grid grid-cols-2 md:grid-cols-3 gap-4")
    #     for a in x[0].find_all("a"):
    #         links.append(a["href"])
    #     info = {
    #         "title": title,
    #         "tags": tags,
    #         "img_url": img_url,
    #         "rating": rating,
    #         "studio": studio,
    #         "source": source,
    #         "episodes": episodes,
    #         "summary": summary,
    #         "links": links
    #     }
    #     return info

