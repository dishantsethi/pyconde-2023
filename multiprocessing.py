from multiprocess import Pool
import requests
from timer import timer

URL = "https://httpbin.org/uuid"

def fetch():
    res = requests.get(URL)
    print(res.json()["uuid"])

@timer(1,1)
def main():
    with Pool() as pool:
        pool.starmap(fetch, [() for _ in range(0,100)])
    