import asyncio


async def fetch_data():
    print("fetching data")
    await asyncio.sleep(2)
    print("finished fetching")
    return {"data": 1}


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(.5)


async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_numbers())


    print("in the main loop")
    value = await task1
    print(value)
    await task2




if __name__ == "__main__":

    asyncio.run(main())