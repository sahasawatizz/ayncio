import asyncio

async def main():
    print ("main coroutine start")

    task = asyncio.current_task()
    print(task)

asyncio.run(main)