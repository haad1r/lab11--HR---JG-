# https://github.com/haad1r/lab11--HR---JG-

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


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Error: Cannot divide by 0.")
    return b/a


def log(a, b):
    if a <= 0 or a == 1:
        raise ValueError("Error: Base a must be positibe but not 1.")
    if b <= 0:
        raise ValueError("Error: The value must be positive.")
    return math.log(b, a)


def exp(a, b):
    return a**b
