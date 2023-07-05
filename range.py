"""
Title: Range Function
Name: Jonah Honsberger
Date: 09/20/2022 [MM-DD-YYYY]
"""

#  Program to pick 6 different random whole numbers in the range 1 to 49
#  and to then count the number of additional draws until all 6 numbers match
import random
a = list(range(1, 50))
# quick pick for the user's numbers
random.shuffle(a)  # permuting the list
b = a[0:6]
print("your lucky numbers are..")
print(sorted(b))
n = 0  # counter for the number of draws
d = 0  # number of matches in each draw
# loop until the user matches 6 numbers
while d < 6:
   # Update the draw counter
   n = n + 1
   # Print an update every one hundred thousand draws
   if n % 100000 == 0:
      print("draws:", n)
   # Pick the winning numbers
   random.shuffle(a)  # permuting the list
   c = a[0:6]  # taking a slice
   # d is the number of matches
   d = len(set(b).intersection(set(c)))
print("it took", n, "draws to match 6 numbers")