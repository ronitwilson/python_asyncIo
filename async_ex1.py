import time
import asyncio
from datetime import datetime
import click

async def sleep_and_print(sleep_time):
    print("starting to sleep {} ".format(sleep_time))
    await asyncio.sleep(sleep_time)
    print("Have slept {} secs".format(sleep_time))
    return sleep_time

# start = datetime.now()
# print([sleep_and_print(3), sleep_and_print(6)])
# click.secho("{}".format(datetime.now()- start), bold=True, bg='blue', fg='white')

async def main():
    co_routine_list = []
    for i in range(1,11):
        co_routine_list.append(sleep_and_print(i))        
    results = await asyncio.gather(*co_routine_list)
    print(results)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# asyncio.run(main())
