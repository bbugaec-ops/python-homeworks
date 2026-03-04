"""
Завдання 2
Напиши програму, яка запускає одночасно три асинхронні функції:

download_file_1() чекає 3 секунди і друкує "File 1 downloaded"
download_file_2() чекає 2 секунди і друкує "File 2 downloaded"
download_file_3() чекає 1 секунду і друкує "File 3 downloaded"
Запусти всі три функції одночасно за допомогою asyncio.gather() """

import asyncio
import time


async def download_file_1():
    print("Пуск першої програми")
    time.sleep(3)


async def download_file_2():
    print("Пуск другої програми")
    time.sleep(2)


async def download_file_3():
    print("ПУск третьої програми")
    time.sleep(1)


asyncio.run(download_file_1())
asyncio.run(download_file_2())
asyncio.run(download_file_3())