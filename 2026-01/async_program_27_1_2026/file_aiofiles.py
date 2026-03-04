"""   Завдання 3

Напиши функцію async_write_file(filename, text), яка асинхронно записує переданий текст у файл.
Напиши функцію async_read_file(filename), яка асинхронно читає файл і виводить його вміст.
Використай asyncio.gather(), щоб записати 3 різних файли одночасно, а потім їх прочитати.

Треба використовувати aiofiles для роботи з файлами без блокування головного потоку."""


import asyncio
import aiofiles

async def async_write_file(filename: str, text: str) -> None:
    async with aiofiles.open(filename, "w", encoding="utf-8") as f:
        await f.write(text)

async def async_read_file(filename: str) -> str:
    async with aiofiles.open(filename, "r", encoding="utf-8") as f:
        content = await f.read()
    print(f"\n--- {filename} ---\n{content}")
    return content

async def main():
    files_data = [
        ("file1.txt", "Привіт файл 1\nРядок 2."),
        ("file2.txt", "Файл 2: асинхронний запис через aiofiles."),
        ("file3.txt", "Файл 3: asyncio.gather() робить все паралельно."),
    ]

    await asyncio.gather(*(async_write_file(n, t) for n, t in files_data))
    await asyncio.gather(*(async_read_file(n) for n, _ in files_data))

if __name__ == "__main__":
    asyncio.run(main())
