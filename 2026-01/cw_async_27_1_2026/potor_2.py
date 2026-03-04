import random
import threading
import time
from queue import Queue
import asyncio
#
# def task(name):
#     print(f"{name} start")
#     time.sleep(2)
#     print(f"{name} finish")
#
# def main():
#     for t in ['a','b','c']:                    Синхронний варіант
#         task(t)
#
#
# if __name__ == '__main__':
#     main()

#
# async def task(name):
#     print(f"{name} start")
#     await asyncio.sleep(2)
#     print(f"{name} finish")                           #  Асінхронний варіант
#
#
# async def main():
#     await asyncio.gather(task('a'), task('b'), task('c'))
#
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
#
# async def task(name):
#     print(f"{name} start")
#     await asyncio.sleep(2)
#     print(f"{name} finish")


import requests
import aiohttp

urls = ['https://itstep.dp.ua/', 'https://itstep.us/', 'https://itstep.dp.ua/', 'https://itstep.us/',
        'https://itstep.dp.ua/','https://itstep.us/']
start = time.time()
for url in urls:
    r = requests.get(url)
    print(f" get {len(r.text)} symbols")
print("time:", time.time() - start)


async def getUrl(session, url):
    async with session.get(url) as resp:
        text = await resp.text()
        print(f"get {len(text)} symbols")
        return text


# async def hello(name):
#     delay = random.randint(1,3)
#     await asyncio.sleep(delay)
#     print(f"Hello, {name}, wait {delay}")
#
async def main():
#     names = ['Bill','Bob','Nikola']
#     tasks = [hello(n) for n in names]
    global urls
    async with aiohttp.ClientSession() as session:
        tasks = [getUrl(session, url) for url in urls]
        await asyncio.gather(*tasks)
#

if __name__ == '__main__':
    asyncio.run(main())
