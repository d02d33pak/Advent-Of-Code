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
<<<<<<< HEAD
        print("File not found")
=======
        print("Invalid Day")
>>>>>>> 619429d (day4 part1 done, added check for day input)

    CHOICE = input("Continue? (y/n) ").lower()
