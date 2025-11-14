"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math


def add(a, b):
    a + b


def subtract(a, b):
    a - b


def multiply(a, b):
    a * b


def divide(a, b):
    try:
        b / a
    except ZeroDivisionError:
        raise  # raise ZeroDivisionError if a == 0


def logarithm(a, b):
    try:
        math.log(a, b)
    except ValueError:  # use math library/raise ValueError
        raise


def exponent(a, b):
    a**b
