# https://github.com/HoangKhoi1234/lab11-MHK-JZ
# Partner 1: Mai Hoang Khoi
# Partner 2: Jessica Zhang
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math


def square_root(a):
    # raise ValueError if a < 0
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError("square_root requires a non-negative number")


def hypotenuse(a, b):
    # can have negative nums
    return math.hypot(a, b)


# First example
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    # raise ZeroDivisionError if a == 0
    if a == 0:
        raise ZeroDivisionError("a cannot be zero")
    return b / a


def logarithm(a, b):
    # log base a of b; raise ValueError for an invalid base or argument
    try:
        if a <= 0 or a == 1 or b <= 0:
            raise ValueError("invalid base or argument for logarithm")
        return math.log(b, a)
    except TypeError:
        raise ValueError("logarithm requires numeric inputs")


def exponent(a, b):
    return a ** b


# Aliases so both naming styles used in the lab instructions work
mul = multiply
div = divide
exp = exponent
