import asyncio

HOST = '127.0.0.1'
PORT = 8080

async def main():
    reader, writer = await asyncio.open_connection(HOST,PORT)
    print("Connected async server")

    writer.write(b"Hello from async client")
    await writer.drain()

    data = await reader.read(1024)
    print("Server responce:", data.decode())

    writer.close()
    await writer.wait_closed()
    print("Client closed")


if __name__ == '__main__':
    asyncio.run(main())