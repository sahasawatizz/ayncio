import asyncio
import time

#coroutine use for a tak

async def task_coro(value):
    #report a message
    print(f'{time.ctime()}task {value} executing')
    #sleep for a moment
    await asyncio.sleep(1)

#coroutine used for the entry point
async def main():
    print(f'{time.ctime()}main starting.')
    coros = [task_coro(i)for i in range (100000000000)]

    await asyncio.gather(*coros)

    print(f'{time.ctime()}main done')

asyncio.run(main())