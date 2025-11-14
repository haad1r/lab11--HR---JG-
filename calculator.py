"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

<<<<<<< HEAD
def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise

def hypotenuse(a,b):
    return math.hypot(a,b)
=======
>>>>>>> 452342af86a48c98882f15cc0bb26b41133fbc6c

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    try:
        return b / a
    except ZeroDivisionError:
        raise  # raise ZeroDivisionError if a == 0


def logarithm(a, b):
    try:
<<<<<<< HEAD
        return math.log(a,b)
    except ValueError: # use math library/raise ValueError
=======
        math.log(a, b)
    except ValueError:  # use math library/raise ValueError
>>>>>>> 452342af86a48c98882f15cc0bb26b41133fbc6c
        raise


def exponent(a, b):
    a**b
