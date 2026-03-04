import asyncio


HOST = '127.0.0.1'
PORT = 8080

clients = set()

async def handle_client(reader:asyncio.StreamReader, writer:asyncio.StreamWriter):
    addr = writer.get_extra_info("peername")
    print(f"New client connected: {addr}")

    clients.add(writer)

    try:
        while True:
            data = await reader.read(1024)
            if not data:
                break

            message = data.decode().strip()
            print(f"{addr}: {message}")

            for client in list(clients):
                if client != writer:
                    client.write(f"{addr}:{message}\n".encode())
                    await client.drain()

    except asyncio.CancelledError:
        pass

    finally:
        print(f"Client disconnect:{addr}")
        clients.discard(writer)
        writer.close()
        await writer.wait_closed()






async def main():
    server = await asyncio.start_server(handle_client,HOST,PORT)
    print("Async server started ")

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())