import asyncio

def _write(filename, text):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


def _read(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()


async def async_write_file(filename, text):
    await asyncio.to_thread(_write, filename, text)


async def async_read_file(filename):
    content = await asyncio.to_thread(_read, filename)
    print(content)
    

async def main():
    files_data = [
        ("file1.txt", "1"),
        ("file2.txt", "2"),
        ("file3.txt", "3"),
    ]

    await asyncio.gather(
        *(async_write_file(n, t) for n, t in files_data)
    )
    await asyncio.gather(
        *(async_read_file(n) for n, _ in files_data)
    )

if __name__ == "__main__":
    asyncio.run(main())
