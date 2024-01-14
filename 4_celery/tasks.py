from celery_redis import fetch
import timeit

URL = "https://httpbin.org/uuid"

def timer(number,repeat):
    def wrapper(func):
        runs = timeit.repeat(func, number=number, repeat=repeat)
        print(sum(runs) / len(runs))

    return wrapper

@timer(1,1)
def main():
    for i in range(100):
        res = fetch.delay(URL)
        print(res, i)
