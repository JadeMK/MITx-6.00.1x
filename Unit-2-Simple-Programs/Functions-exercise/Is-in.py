"""
(bisection search to determine if a character is in a string.)
Implement the function isIn(char, aStr) recursively to test if char is in aStr 
"""


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    
    # Check if aStr is empty
    if len(aStr) < 1:
        return False

    # Recursive bisection search
    mid_point = len(aStr) // 2
    if mid_point == 0:
        return char == aStr
    elif char == aStr[mid_point]:
        return True
    elif char < aStr[mid_point]:
        return isIn(char, aStr[:mid_point])
    elif char > aStr[mid_point]:
        return isIn(char, aStr[mid_point+1:])


# print(isIn('h', 'eeghlmpqstvvwwy'))
