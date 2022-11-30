# (datetime.datetime => dt namespace)
from datetime import datetime as dt
from dotenv import dotenv_values
import time

# load environment variables
[hosts_temp, redirect, website_list] = dotenv_values(".env").values()

# convert string to a list and remove unneeded characters
website_list = website_list.strip("[]").replace("'", "").split(", ")

# writes blocked websites to hosts file
def write_to_file():
    with open(hosts_temp, "r+") as file:
        contents = file.read()

        # add all websites with redirect if not in host file
        for website in website_list:
            if not (website in contents):
                file.write("\n{}\t{}".format(redirect, website))


# generator expression compares each website against the current line, outputs True or False
# outputs stored in a generator object (iterable)
# write to file if no websites are in the current line
def reset_file():
    with open(hosts_temp, "r+") as file:
        contents = file.readlines()

        # move cursor to starting position
        file.seek(0)

        # check each website in list against each line in file
        # if website isn't there, write to file
        for line in contents:
            if not any(website in line for website in website_list):
                file.write(line)

        # delete all text after cursor end point
        file.truncate()


while True:
    # year, month, day, time: 8am
    work_start = dt(dt.now().year, dt.now().month, dt.now().day, 8)

    # year, month, day, time: 5pm
    work_end = dt(dt.now().year, dt.now().month, dt.now().day, 16)

    # during work hours, write to hosts file adding website and redirect
    if work_start < dt.now() < work_end:
        write_to_file()
    else:
        reset_file()

    time.sleep(5)  # 5 sec delay
