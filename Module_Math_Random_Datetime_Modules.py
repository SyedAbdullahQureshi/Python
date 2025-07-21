# my_module.py

def greet(name):           # greet
    return f"Hello, {name}!"

pi = 3.141                 # constant

def square(n):             # square
    return n * n

# Import Custom Module

import my_module           # import

print(my_module.greet("Ali"))     # greet
print(my_module.pi)               # pi
print(my_module.square(5))        # square


# Math Module

import math                # import

print(math.sqrt(25))       # sqrt
print(math.ceil(2.3))      # ceil
print(math.floor(2.9))     # floor
print(math.pow(2, 3))      # power
print(math.pi)             # pi


# Random Module

import random              # import

print(random.randint(1, 100))     # integer
print(random.choice(["Ali", "Sara", "Ayan"]))  # choice
print(random.random())            # float (0-1)
print(random.uniform(10, 20))     # float range

# Datetime Module

import datetime            # import

now = datetime.datetime.now()     # now
print("Current:", now)

today = datetime.date.today()     # today
print("Today:", today)

# Custom Date
d = datetime.date(2025, 7, 21)    # create
print("Custom:", d)

# Format
print("Formatted:", now.strftime("%d-%b-%Y %H:%M"))   # format
