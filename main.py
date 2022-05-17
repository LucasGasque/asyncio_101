import asyncio
import time


class Request1:
    @classmethod
    async def get(self):
        print("Request 1 started")
        await asyncio.sleep(2)
        print("Request 1 finished")
        return "response1"


class Request2:
    @classmethod
    async def get(self):
        print("Request 2 started")
        await asyncio.sleep(2)
        print("Request 2 finished")
        return "response2"


async def slow_func():
    start = time.perf_counter()

    response1 = await Request1.get()
    response2 = await Request2.get()

    end = time.perf_counter()

    print(f"slow_func took {end-start} seconds")

    return response1, response2


async def fast_func():
    start = time.perf_counter()

    response1, response2 = await asyncio.gather(
        Request1.get(),
        Request2.get(),
    )

    end = time.perf_counter()

    print(f"slow_func took {end-start} seconds")

    return response1, response2


asyncio.run(slow_func())
asyncio.run(fast_func())

