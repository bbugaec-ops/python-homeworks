"""   ЗАВДАННЯ: Async Chat

РІВЕНЬ 1 (обовʼязковий, базовий)
Завдання
Додати нікнейм користувача
після підключення клієнт надсилає своє імʼя
Сервер:
зберігає nickname → writer
показує повідомлення у форматі [Anna]: Привіт всім
При підключенні нового користувача: сервер надсилає всім
Anna joined the chat
Підказка
перше повідомлення після connect — це імʼя
зберігати клієнтів у dict
"""

import asyncio

clients = {}  # nick -> writer

async def broadcast(msg: str):
    for w in clients.values():
        w.write((msg + "\n").encode())
        await w.drain()

async def handle(reader, writer):
    nick = (await reader.readline()).decode().strip()
    clients[nick] = writer
    await broadcast(f"{nick} joined")

    try:
        while data := await reader.readline():
            msg = data.decode().strip()
            await broadcast(f"[{nick}]: {msg}")
    finally:
        clients.pop(nick, None)
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle, "127.0.0.1", 8888)
    async with server:
        await server.serve_forever()

asyncio.run(main())
