import asyncio

async def f1(x: int)-> None:
    print(f'starting {x}')
    await asyncio.sleep(x)
    print(f'hello from {x}')

async def f2():
    raise ValueError('Error')

async def f3():
    2 * 3 * (4 - None)

async def task_groups()-> int:
    try:
        async with asyncio.TaskGroup() as tg:
            for i in range(5):
                tg.create_task(f1(i))

            tg.create_task(f2())
            tg.create_task(f3())

    # except ExceptionGroup as eg:
    #     print(dir(eg))
    #     print(f"got {eg}")
    except* ValueError as ve:
        print(dir(ve))
        print(f'got {ve}')

    print('Done')
    return 0

def main():
    asyncio.run(task_groups())

if __name__ == '__main__':
    main()
