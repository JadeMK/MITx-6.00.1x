"""
implement the function getAvailableLetters that takes in one parameter -
a listof letters, lettersGuessed. This function returns a string that is
comprised oflowercase English letters - all lowercase English letters that
are not in lettersGuessed.

Example Usage:

>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz
"""


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    available_list = [item for item in list(map(chr, range(97, 123))) if item not in lettersGuessed]
    return "".join(available_list)
