"""
iterative function, gcdIter(a, b)
begin with a test value equal to the smaller of the two input arguments,
and iteratively reduce this test value by 1 until you either reach a case
where the test divides both a and b without remainder, or you reach 1.
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = 1
    if a > b:
        a, b = b, a
    for i in range(a, 1, -1):
        if b % i == 0 and a % i == 0:
            gcd = i
            break
    return gcd


# print(gcdIter(78696, 19332))
