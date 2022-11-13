import asyncio

async def sleep_five():
    await asyncio.sleep(5)
    print("slept for 5 secs")

async def sleep_three_then_five():
    await asyncio.sleep(3)
    print("slept for 3 secs")
    await sleep_five()


async def main():
    await asyncio.gather(sleep_five(), sleep_three_then_five())

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
