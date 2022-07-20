from time import perf_counter

import requests

# import aiohttp

url = "https://jsonplaceholder.typicode.com/todos/{}"
# symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results = []


def get_request():
    for i in range(1, 201):
        r = requests.get(url.format(i))
        results.append(r.json())

    return results


def main():

    res = get_request()

    print(res)


if __name__ == "__main__":
    start = perf_counter()
    main()
    total_time = perf_counter() - start
    print(f"It took {total_time} seconds to make 200 API calls")
