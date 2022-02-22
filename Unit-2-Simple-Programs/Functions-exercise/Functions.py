"""
square: takes in one number and returns the square of that number
evalQuadratic: takes in four numbers and returns a single number
fourthPower: returns one's value raised to the fourth power using square()
odd: returns True when the number is odd and False otherwise
"""


def square(x):
    '''
    x: int or float.
    '''
    # Your code here
    return x ** 2


def evalQuadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    # Your code here
    return a * (x**2) + b * x + c


def fourthPower(x):
    '''
    x: int or float.
    '''
    # Your code here
    return square(x) ** 2


def odd(x):
    '''
    x: int

    returns: True if x is odd, False otherwise
    '''
    # Your code here
    return x % 2 != 0
