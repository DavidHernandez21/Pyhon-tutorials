from time import perf_counter

import aiohttp

import asyncio

# import os
# To work with the .env file
# from dotenv import load_dotenv
# load_dotenv()

# API_KEY = "RIAR437J81J0ZPM6"
# url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
url = "https://jsonplaceholder.typicode.com/todos/{}"
# symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results = []


# def get_tasks(session):
#     tasks = []
#     for symbol in symbols:
#         tasks.append(asyncio.create_task(session.get(url.format(symbol, API_KEY), ssl=False)))
#     return tasks


async def get_symbols():
    async with aiohttp.ClientSession() as session:

        # tasks = get_tasks(session)
        # you could also do
        tasks = [
            asyncio.create_task(session.get(url.format(symbol), ssl=False))
            for symbol in range(1, 201)
        ]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())
        print(f"aiohttp session is closed: {session.closed}")

    print(f"aiohttp session is closed: {session.closed}")
    return results


async def main():
    # start = perf_counter()
    task1 = asyncio.create_task(get_symbols())

    print("in the main loop")
    res = await task1
    # total_time = perf_counter() - start
    # print(f"It took {total_time} seconds to make {len(res)} API calls")
    print(len(res))


if __name__ == "__main__":
    start = perf_counter()
    asyncio.run(main())
    total_time = perf_counter() - start
    print(f"It took {total_time} seconds to make 200 API calls")
