#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else -(-number % 10)
output = ""
if last_digit == 0:
    output = "and is 0"
elif last_digit > 5:
    output = "and is greater than 5"
else:
    output = "and is less than 6 and not 0"
print("Last digit of {} is {} {}".format(number, last_digit, output), end="\n")
