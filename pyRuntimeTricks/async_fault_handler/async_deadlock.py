import asyncio

from async_fault_handler import start_tracing

lock1 = asyncio.Lock()
lock2 = asyncio.Lock()


async def f1():
    async with lock1:
        await asyncio.sleep(1)
        async with lock2:
            print("hey 1")


async def f2():
    async with lock2:
        await asyncio.sleep(1)
        async with lock1:
            print("hey 2")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    start_tracing(loop, 3, repeat=False)

    loop.run_until_complete(asyncio.gather(
        f1(),
        f2(),
    ))