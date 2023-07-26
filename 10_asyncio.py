import asyncio
import time

class AsyncContextManager:
    async def __aenter__(self):
        print(f'{time.ctime()}>entering the context manager')
        await asyncio.sleep(0.5)

    async def __aexit__(self, exc_type,exc,tb):
        print(f'{time.ctime()}>exitting the context manager')
        await asyncio.sleep(0.5)

async def custom_coroutine():
    async with AsyncContextManager() as manager:
        print(f'{time.ctime()}within the manager')

asyncio.run(custom_coroutine())