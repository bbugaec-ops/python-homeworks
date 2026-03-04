"""   Завдання 1
Напиши функцію async_counter(n), яка виводить числа від 1 до n з паузою в 1 секунду між виведенням.
Використай asyncio.sleep() для затримки.
"""

import asyncio


async def async_counter(n):
    for i in range(1, n+1):
        print(i)
        await asyncio.sleep(1)


asyncio.run(async_counter(5))



