# (datetime.datetime => dt namespace)
from datetime import datetime as dt
from dotenv import dotenv_values
import time

[hosts_temp, redirect, website_list] = dotenv_values(".env").values()

while True:
    # year, month, day, time: 8am
    work_start = dt(dt.now().year, dt.now().month, dt.now().day, 8)

    # year, month, day, time: 5pm
    work_end = dt(dt.now().year, dt.now().month, dt.now().day, 17)

    if work_start < dt.now() < dt.now() < work_end:
        print("working hours...")

    else:
        print("non-working hours...")

    time.sleep(5)  # 5 sec delay
