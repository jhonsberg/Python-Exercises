"""
Title: Hundred
Name: Jonah Honsberger
Date: 10/28/2022 [MM-DD-YYYY]
"""

from datetime import datetime

# calculate what year you will turn 100
name = input('Enter your name: \n')
age = int(input('Enter your age: \n'))
year = int((100-age) + datetime.now().year)

print('Hello ' + name +', You will turn 100 in the year ' + str(year))