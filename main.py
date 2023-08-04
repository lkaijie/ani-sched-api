# from ani_sched import *
# from ani_sched import News, get as test
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
    # schedule.get_sched("summer", 201)
    print(schedule.get_sched())

if __name__ == "__main__":
    test()