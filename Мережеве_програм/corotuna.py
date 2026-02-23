import asyncio

async def print_one():
    await asyncio.sleep(2)
    print("print_one")

async def print_two():
    await asyncio.sleep(1)
    print("print_two")

async def main():
    await asyncio.gather(
        print_one(),
        print_two()
    )

if __name__ == "__main__":
    asyncio.run(main())
