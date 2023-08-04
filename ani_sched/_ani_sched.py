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

    def get_sched(self, season=None, year=None) -> None:
        """Returns a list of dicts containing the seasonal anime schedule
        """
        if not season:
            entries = self._parse_url(self.lc_url)
            return entries
        else:
            if not season and not year:
                raise ValueError("Must provide season and year")
            else:
                # example url: https://www.livechart.me/summer-2021/tv
                endpoint = f"{self.lc_url}/{season}-{year}/tv"
                entries = self._parse_feed(endpoint)
                print(entries)
    
    def get(self) -> None:
        """Returns a list of dicts containing the entries of the feed
        """
        print("Getting news...")
        entries = self._parse_feed(self.url)
        return entries
                
if __name__ == "__main__":
    anisched = AniSched()
    anisched.get_sched("summer", 2021)