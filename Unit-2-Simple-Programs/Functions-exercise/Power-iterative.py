"""
iterative function:
calculates the exponential base ** exp by using successive multiplication.
(without ** operator)
"""


def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    while exp > 0:
        result *= base
        exp -=1
    return result


# print("test", iterPower(-3.14, 8))
