"""
Main module to run all days from one place
Author: Deepak Talan
Github: @d02d33pak
"""

import os

CHOICE = "y"

while CHOICE == "y":

    day = "day_" + input("Enter Day: ").zfill(2)
    os.system("python3 " + day)

    CHOICE = input("Continue? (y/n) ").lower()
