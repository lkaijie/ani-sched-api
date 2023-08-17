<!-- 
<div>
![Tests](https://github.com/lkaijie/ani-sched-api/workflows/PyTests/badge.svg "CI build status: Check JSON files")
[![Downloads](https://pepy.tech/badge/ani-sched/month)](https://pepy.tech/project/ani-sched)
</div> -->
<div align="center" style="margin-bottom:20px">
    <span style="margin-right:10px">
        <img src="https://github.com/lkaijie/ani-sched-api/workflows/PyTests/badge.svg" alt="Tests">
    </span>
    <span style="margin-left:10px">
        <a href="https://pepy.tech/badge/ani-sched">
            <img src="https://static.pepy.tech/badge/ani-sched/month" alt="Downloads">
        </a>
    </span>


</div>

# Python Anime Schedule API
[![Version](https://img.shields.io/pypi/v/ani-sched.svg?color=informational)](https://pypi.org/project/ani-sched/)

A lightweight API for gathering anime schedules from [MyAnimeList](https://myanimelist.net) or anime news and announcements from [LiveChart](https://livechart.me).


## Installation and Usage

To install the library:

```
pip install -U ani-sched
```

To import the library:

```python
from ani_sched import *
```

## Example

To call the API, you need to create an object.
    
```python
from ani_sched import AniSched

api = AniSched()

fall_2022 = api.season(year=2022, season='fall') # gets the animes of Fall 2022

print(fall["TV (New)"][7]["title"]) # prints the title of the 8th most popular TV anime of Fall 2022

# output: "Bocchi the Rock!"

```
####
