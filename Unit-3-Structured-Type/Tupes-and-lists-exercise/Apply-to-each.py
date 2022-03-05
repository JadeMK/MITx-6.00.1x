"""
provide an expression using applyToEach, so that after evaluation testList has
the indicated value.
"""


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

testList = [1, -4, 8, -9]


# Return -> [1, 4, 8, 9]
applyToEach(testList, abs)


# Return -> [2, -3, 9, -8]
def add_one(a):
    return a + 1

applyToEach(testList, add_one)


# Return -> [1, 16, 64, 81]
def abs_squared(a):
    return abs(a) ** 2

applyToEach(testList, abs_square)
