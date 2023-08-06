import datetime
from ani_sched import _base
from ani_sched._base import _Base
import ani_sched.config as config
from typing import List, Dict


class AniSched(_Base):
    def __init__(self, timeout: int = config.TIMEOUT) -> None:
        super().__init__(timeout)
        self.headline_url = config.HEADLINE_ENDPOINT
        self.recently_aired_url = config.RECENTLY_AIRED_ENDPOINT
        self.lc_url = config.LC_ENDPOINT
        self.get_redirect(self.lc_url)
        
    def get_redirect(self, url: str) -> str:
        # prob can be removed at some point
        url = self._get_redirect(url)
        self.lc_url2 = url+config.QUERY

    def get_sched(self, season=None, year=None) -> None:
        """Returns a dict of dicts containing the seasonal anime schedule
        """
        def _get_current_season(self) -> str:
            """example output: winter-2021"""
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
        
        def _extract(self, soup):
            """Returns a dict of dicts containing the seasonal anime schedule

            Args:
                soup (Beautiful Soup object): Of the anime section of the website

            Returns:
                dict: returns a dict containing the anime schedule
            """
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
                
                source = "Unknown"
                episodes = "Unknown"
                for y in x.find("div", class_="anime-metadata"):
                    if y.get("class") == ["anime-source"]:
                        source = y.text
                    elif y.get("class") == ["anime-episodes"]:
                        episodes = y.text
                
                # anime_metadata = x.find("div", class_="anime-metadata")
                # if anime_metadata:
                #     for z in anime_metadata.find_all("div"):
                #         if z.get("class") == ["anime-source"]:
                #             source = z.text
                #         elif z.get("class") == ["anime-episodes"]:
                #             episodes = z.text

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
            return animes  
        
        if not season:
            season = _get_current_season(self)
            # example url: https://www.livechart.me/winter-2021/tv
            url = f"{self.lc_url}{season}/tv?titles=english"
            entries = self._parse_url(url,type="selenium")
            print(url)
            return _extract(self, entries)
        else:
            if not season and not year:
                raise ValueError("Must provide season and year")
            elif season not in ["winter", "spring", "summer", "fall"]:
                raise ValueError("Season must be one of the following: winter, spring, summer, fall")
            else:
                # example url: https://www.livechart.me/summer-2021/tv
                endpoint = f"{self.lc_url}{season}-{year}/tv?titles=english"
                print(endpoint)
                entries = self._parse_url(endpoint, type="selenium")
                return _extract(self, entries)
    
    def get_news(self) -> None:
        """Returns a list of dicts containing the news entries of the feed
        """
        print("Getting news...")
        entries = self._parse_feed(self.headline_url)
        return entries
    
    def get_recently_aired(self) -> None:
        """Returns a list of dicts containing the recently aired anime
        """
        print("Getting recently aired...")
        entries = self._parse_feed(self.recently_aired_url)
        return entries
        
    
if __name__ == "__main__":
    anisched = AniSched()
    anisched.get_sched("summer", 2021)