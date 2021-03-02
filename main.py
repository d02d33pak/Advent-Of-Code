"""
Main module to run all days from 1 place
Author: Deepak Talan
Github: @d02d33pak
"""

import os

green = True

while(green):

    day = "day_" + input("Enter Day: ").zfill(2)
    os.system("python3 " + day)
    
    choice = input("Continue? (y/n) ").lower()
    green = True if choice == 'y' else False

