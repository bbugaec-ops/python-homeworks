import asyncio

from urllib3.filepost import writer

HOST = '127.0.0.1'
PORT = 8080

async def send_message(writer):
    while True:
        message = await asyncio.to_thread(input)
        writer.write(message.encode())
        await writer.drain()

async def receive_message(reader):
    while True:
        data = await reader.read(1024)
        if not data:
            break
        print(data.decode(),end="")


async def main():
    reader, writer = await asyncio.open_connection(HOST,PORT)
    print("Connected to chat")

    await asyncio.gather(
        send_message(writer),
        receive_message(reader)
    )



if __name__ == '__main__':
    asyncio.run(main())
