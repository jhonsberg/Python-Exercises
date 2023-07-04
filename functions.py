"""
Title: Functions
Name: Jonah Honsberger
Date: 10/06/2022 [MM-DD-YYYY]
"""

# adding strings and vars in a function
def sayhi(name, age):
    print("Hello " + name + ", you are " + age + " years old")

sayhi("Mike", "27")
sayhi("Steve", "17")


# doing equations in a function
def cube(num):
    return num*num*num

result = cube(4)
print(result)


# print a string backwards
def backwards(string: str):
    reversed_string = string[::-1]
    print(reversed_string)

backwards("jumping")


# finds highest number of 3 without max()
one = input('Enter your first number: ')
two = input ('Enter your second number: ')
three = input('Enter your third number: ')

def maximum(a: int, b: int, c: int) -> int:
    highest = max(a, b, c)
    return highest

print('The highest number is ' + maximum(one, two, three))


# find distance between 2 coordinates
import math

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

x1 = int(input('X-Coordinate 1: '))
y1 = int(input('Y-Coordinate 1: '))

x2 = int(input('X-Coordinate 2: '))
y2 = int(input('Y-Coordinate 2: '))

result = distance(x1, y1, x2, y2)
print('The distance between the two points is', result)