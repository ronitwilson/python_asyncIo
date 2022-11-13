import time
from datetime import datetime
import click



def sleep_and_print(sleep_time):
    print("starting to sleep {} ".format(sleep_time))
    time.sleep(sleep_time)
    print("Have slept {} secs".format(sleep_time))
    return sleep_time
    
start = datetime.now()
print([sleep_and_print(3), sleep_and_print(6)])
click.secho("{}".format(datetime.now()- start), bold=True, bg='blue', fg='white')
