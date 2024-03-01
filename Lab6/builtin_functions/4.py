from time import sleep
from math import sqrt

number = int(input())

seconds = int(input())

miliseconds = seconds / 1000

sleep(miliseconds)

square = sqrt(number)

print(f"Square root of {number} after {seconds} is {square}")