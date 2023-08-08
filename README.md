# Ani-Sched API


[![pypi Version](https://img.shields.io/pypi/v/mal-api.svg?color=informational)](https://pypi.org/project/mal-api/)

An unofficial lightweight API for gathering anime schedules from [MyAnimeList](https://myanimelist.net).


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