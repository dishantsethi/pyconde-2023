import requests
from timer import timer

URL = "https://httpbin.org/uuid"

@timer(1, 1)
def main():
    for _ in range(0,100):
        res = requests.get(URL)
        print(res.json()["uuid"])