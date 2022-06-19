import concurrent.futures
import logging
import queue
import random
import threading
import time

def producer(my_queue: queue.Queue, event: threading.Event) -> None:
    """Pretend we're getting a number from the network."""
    while not event.is_set():
        message = random.randint(1, 101)
        logging.info("Producer got message: %s", message)
        my_queue.put(message)

    logging.info("Producer received event. Exiting")

def consumer(my_queue: queue.Queue, event: threading.Event) -> None:
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not my_queue.empty():
        message = my_queue.get()
        logging.info(
            "Consumer storing message: %s (approx size=%d)", message, my_queue.qsize()
        )

    logging.info("Consumer received event. Exiting")

if __name__ == "__main__":
    my_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=my_format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        logging.info("Main: about to set event")
        event.set()