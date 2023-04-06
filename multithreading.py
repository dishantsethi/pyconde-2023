from threading import Thread
from concurrent.futures import ThreadPoolExecutor
import requests
from timer import timer

URL = "https://httpbin.org/uuid"

def fetch(URL):
    res = requests.get(URL)
    print(res.json()["uuid"])

@timer(1,1)
def main():
    with ThreadPoolExecutor(max_workers=40) as thread:
        thread.map(fetch, [URL] * 50)
        thread.shutdown(wait=True)
    