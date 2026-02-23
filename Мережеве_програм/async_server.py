import asyncio


HOST = '127.0.0.1'
PORT = 8080

async def handle_client(reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    print(f"Connected: {addr}")

    data = await reader.read(1024)
    if not data:
        print("No data received")
    else:
        message = data.decode()
        print("Client says:", message)
        writer.write(b"Hello from async server")
        await writer.drain()


    writer.close()
    await writer.wait_closed()
    print(f"Disconnected {addr}")


async def main():
    server = await asyncio.start_server(handle_client,HOST,PORT)
    print("Async server started ")
    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())