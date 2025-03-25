import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def square_root(a):
    if a < 0:
        return "Error! Cannot compute square root of a negative number."
    return math.sqrt(a)
