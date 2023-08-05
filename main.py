# from ani_sched import *
# from ani_sched import News, get as test
import json
import random
from ani_sched import *

# def main() -> None:
#     news = News().get()
#     # print(news)
#     print(type(news))
#     print(type(news[0]))
#     print(news[0].keys())
#     print(news[0]["title"])

# def main2():
#     news = News()
#     print(news)
def main3():
    test = AniSched()
    test2 = News()
    news = test.get()
    print(news)

def test():
    schedule = AniSched()
    error = schedule.get_sched("summer", 201)
    try:
        first_item = error[next(iter(error))]
        print(first_item)
    except:
        print("Error")
    normal = schedule.get_sched()
    # print(random.choice(normal))
    
    json2 = json.dumps(normal, indent=4)
    with open("normal.json", "w") as f:
        f.write(json2)
    
    first_item = normal[next(iter(normal))]
    print(first_item)
    year = schedule.get_sched("winter", 2024)
    # print(random.choice(year))
    # first_item = year[next(iter(year))]
    # print(year)
    json1 = json.dumps(year, indent=4)
    with open("winter2024.json", "w") as f:
        f.write(json1)
    
if __name__ == "__main__":
    test()