"""
Main module to run all days from one place
Author: Deepak Talan
Github: @d02d33pak
"""

import os

choice = 'y'

while choice == 'y':

    day = "day_" + input("Enter Day: ").zfill(2)
    os.system("python3 " + day)
    
    choice = input("Continue? (y/n) ").lower()
