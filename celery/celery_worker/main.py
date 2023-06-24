import concurrent.futures
from time import perf_counter_ns

from tasks import add

# import time


def work(timeout: int) -> str:
    result = add.delay(2, 2)
    # print(f"result is ready: {result.ready()}")
    # # print(dir(result))
    # print(result.status)
    # print(result.state)
    # print(result.successful())
    # print(result.backend)
    # start = time.perf_counter()
    # print(result.wait())
    # print(result.get(timeout=timeout))
    # print(f"result is ready: {result.ready()}")
    # print(dir(result))
    # print(result.status)
    # print(result.state)
    # print(result.successful())
    value = result.get(timeout=timeout)
    return f'result state: {result.state}, result was succesful: {result.successful()}, result value: {value}'
    # print(time.perf_counter() - start)
    # r = app.AsyncResult("240407a3-d992-4403-a2a3-469dddcf5b74")
    # print(dir(app.AsyncResult("240407a3-d992-4403-a2a3-469dddcf5b74")))
    # print(r.name)
    # print(r.traceback)
    # print(r.result)
    # print(r.queue)
    # print(r.info)
    # print(r.failed())
    # print(r.date_done)
    # print(r.worker)
    # print(r.id)
    # print(r.get())


def concurrent_map():
    timeouts = [10 for _ in range(30)]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = executor.map(work, timeouts, timeout=20)
        # print(result.result())
    for v in result:
        print(v)


def concurrent_submit():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = (executor.submit(work, 10) for _ in range(30))

        for future in concurrent.futures.as_completed(results, timeout=20):
            try:
                # result =
                print(future.result())
            except concurrent.futures.TimeoutError as e:
                print(e)


def main():
    start = perf_counter_ns()
    # concurrent_submit()
    concurrent_map()

    print(f'process took {(perf_counter_ns() - start) * 10e-10:.2f}s')


if __name__ == '__main__':
    main()
