from tasks import add

# import time


def main():
    result = add.delay(2, 2)
    print(result.ready())
    # print(dir(result))
    print(result.status)
    print(result.state)
    print(result.successful())
    # print(result.backend)
    # start = time.perf_counter()
    # print(result.wait())
    print(result.get(timeout=5))
    print(result.ready())
    # print(dir(result))
    print(result.status)
    print(result.state)
    print(result.successful())
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


if __name__ == "__main__":
    main()
