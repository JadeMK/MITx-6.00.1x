"""
A clever mathematical trick (due to Euclid) makes it easy to find
greatest common divisors. Suppose that a and b are two positive integers:

If b = 0, then the answer is a
Otherwise, gcd(a, b) is the same as gcd(b, a % b)

Write a function gcdRecur(a, b) that implements this idea recursively.
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


# print(gcdRecur(1029, 1071))
