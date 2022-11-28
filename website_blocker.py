# (datetime.datetime => dt namespace)
from datetime import datetime as dt
from dotenv import dotenv_values
import time

# load environment variables
[hosts_temp, redirect, website_list] = dotenv_values(".env").values()

# convert string to a list and remove unneeded characters
website_list = website_list.strip("[]").replace("'", "").split(", ")


def write_to_file():
    with open("hosts_temp", "r+") as file:
        contents = file.read()
        for website in website_list:
            if not (website in contents):
                file.write("\n{}\t{}".format(redirect, website))


while True:
    # year, month, day, time: 8am
    work_start = dt(dt.now().year, dt.now().month, dt.now().day, 8)

    # year, month, day, time: 5pm
    work_end = dt(dt.now().year, dt.now().month, dt.now().day, 23)

    # during work hours, write to hosts file adding website and redirect
    if work_start < dt.now() < work_end:
        write_to_file()
    else:
        pass

    time.sleep(5)  # 5 sec delay
