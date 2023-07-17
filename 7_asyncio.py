import asyncio
import time
def blocking_task():
    print(f'{time.ctime()}Task starting....')

    time.sleep(2)

    print(f'{time.ctime()}Task done')

async def main():
    print(f'{time.ctime()}Main running the blocking task')

    coro = asyncio.to_thread(blocking_task)

    task = asyncio.create_task(coro)

    print(f'{time.ctime()}Main doing other thing')

    await asyncio.sleep(0)

    await task

asyncio.run(main())