from ani_sched import _base
from ani_sched._base import _Base
import ani_sched.config as config
from typing import List, Dict


class News(_Base):
    def __init__(self, timeout: int = config.TIMEOUT) -> None:
        super().__init__(timeout)
        self.url = config.HEADLINE_ENDPOINT
        
        # testing
        
    def get(self) -> None:
        """Returns a list of dicts containing the entries of the feed
        """
        print("Getting news...")
        entries = self._parse_feed(self.url)
        return entries
    
def get() -> List[Dict]:
    """Returns a list of dicts containing the entries of the feed
    """
    print("Getting news...")
    entries = _Base._parse_feed(config.HEADLINE_ENDPOINT)
    return entries