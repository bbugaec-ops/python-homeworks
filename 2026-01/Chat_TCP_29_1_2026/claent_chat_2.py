import asyncio

async def main():
    nick = input("nick: ").strip()

    reader, writer = await asyncio.open_connection("127.0.0.1", 8888)

    writer.write((nick + "\n").encode())
    await writer.drain()

    async def read():
        while data := await reader.readline():
            print(data.decode().strip())

    async def write():
        while True:
            msg = await asyncio.to_thread(input, "")
            writer.write((msg + "\n").encode())
            await writer.drain()

    await asyncio.gather(read(), write())

asyncio.run(main())
