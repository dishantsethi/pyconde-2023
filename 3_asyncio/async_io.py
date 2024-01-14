import asyncio
import aiohttp
from timer import timer

URL = "https://httpbin.org/uuid"

async def fetch(session, url):
    async with session.get(url) as response:
        res = await response.json()
        print(res["uuid"])

async def main():
    async with aiohttp.ClientSession() as session:
        task = [fetch(session, URL) for _ in range(100)]
        await asyncio.gather(*task)
    
@timer(1,1)
def func():
    asyncio.run(main())