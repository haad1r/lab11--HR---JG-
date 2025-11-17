# https://github.com/haad1r/lab11--HR---JG-
# Partner 1: Haadi Rattansi
# Partner 2: Juan Garcia

import math


def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise


def hypotenuse(a, b):
    return math.hypot(a, b)


def add(a, b):
    return a+b


def subtract(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Error: Cannot divide by 0.")
    return b/a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Error: Base a must be positibe but not 1.")
    if b <= 0:
        raise ValueError("Error: The value must be positive.")
    return math.log(b, a)


def exp(a, b):
    return a**b
