import concurrent.futures
import logging
import time


def thread_function(name: int) -> None:
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    my_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=my_format, level=logging.INFO, datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
