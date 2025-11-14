"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise

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
        raise# raise ZeroDivisionError if a == 0

def logarithm(a, b):
    try:
        return math.log(a,b)
    except ValueError: # use math library/raise ValueError
        raise

def exponent(a, b):
    a**b


