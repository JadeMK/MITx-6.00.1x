"""
Hangman Part - 1/3

First, implement the function isWordGuessed that takes in two parameters -
a string, secretWord, and a list of letters, lettersGuessed. This function
returns a boolean - True if secretWord has been guessed (ie, all the letters
of secretWord are in lettersGuessed) and False otherwise.
"""


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
