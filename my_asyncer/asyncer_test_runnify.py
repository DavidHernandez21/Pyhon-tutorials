import anyio
import asyncer


async def do_work(name: str, sleep: float) -> str:
    await anyio.sleep(sleep)
    return f"Hello, {name}"


async def main(name: str, sleep: float):
    main_result = await do_work(name=name, sleep=sleep)
    return main_result


result = asyncer.runnify(main)(name="David", sleep=5)
print(result)
