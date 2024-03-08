"""


Created by Rana jay on Mahashivratri ..
Asynchronous framework -> concurrent programming
non-blocking I/O

How does python achieve multiple tasks at once?
1 OS share CPU resources -> multi-sharing
2 Using Threads
3 Asynchronous Programming

event loop

4 components of tornado
1. web framework -> RequestHandler
2. Client + server -> HTTP
3. Asynchronous library -> IOloop + IOstream
4. coroutine library -> tornado.gen

"""


import asyncio


e_loop = asyncio.get_event_loop()


async def hello():
    print("Searching")
    print("CPU is free")
    print("hi")
    print("hello")
    await asyncio.sleep(3)
    print("waiting for task 11")
    await asyncio.sleep(2)
    print("waiting for task 2")
    # await asyncio.sleep(2)
    print("waiting for task 23")
    # await asyncio.sleep(2)
    print("waiting for task 25")


async def hii():
    print("Searching 2")
    print("CPU is free 2")
    print("hi 2")
    print("hello 2")
    await asyncio.sleep(3)
    print("waiting for task 11 2")
    await asyncio.sleep(2)
    print("waiting for task 2 2")
    # await asyncio.sleep(2)
    print("waiting for task 23 2")
    # await asyncio.sleep(2)
    print("waiting for task 25 2")


def rj():
    print("Hello  world")
    e_loop.run_until_complete(hello())
    e_loop.run_until_complete(hii())


if __name__ == "__main__":
    rj()
