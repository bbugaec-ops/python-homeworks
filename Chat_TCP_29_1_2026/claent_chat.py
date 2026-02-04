# client.py
import asyncio

async def main():
    nick = input("nick: ").strip()
    r, w = await asyncio.open_connection("127.0.0.1", 8888)
    w.write((nick + "\n").encode()); await w.drain()

    async def read():
        while d := await r.readline():
            print(d.decode().strip())

    async def write():
        while True:
            msg = await asyncio.to_thread(input, "")
            w.write((msg + "\n").encode()); await w.drain()

    await asyncio.gather(read(), write())

asyncio.run(main())
