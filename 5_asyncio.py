import random
import asyncio
import time

async def task_coro(arg):
    value = random.random()
    await asyncio.sleep(value)
    print(f'{time.ctime()}>task{arg}done with{value}')

async def main():
    tasks = [asyncio.create_task(task_coro(i))for i in range(10)]

    done,pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    print(f'{time.ctime()}All done')

asyncio.run(main())