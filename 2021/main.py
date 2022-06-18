"""
Main module to run all days from one place
Author: Deepak Talan
Github: @d02d33pak
"""

import os

CHOICE = "y"

while CHOICE == "y":

    day = "day_" + input("Enter Day: ").zfill(2)
    if os.path.exists(day):
        os.system("python3 " + day)
    else:
        print("File not found")

    CHOICE = input("Continue? (y/n) ").lower()
