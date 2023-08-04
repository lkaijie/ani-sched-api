from ani_sched import _base
from ani_sched._base import _Base


class Recent(_Base):
    def __init__(self, timeout: int) -> None:
        super().__init__(timeout)
        
    # def 