"""
Problem #3: Test word validity

At this point, we have written code to generate a random hand and display that
hand to the user. We can also ask the user for a word (Python's input) and
score the word (using your getWordScore). However, at this point we have not
written any code to verify that a word given by a player obeys the rules of the
game. A valid word is in the word list; and it is composed entirely of letters
from the current hand. Implement the isValidWord function.
"""


def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    result = False
    hand_copy = hand.copy()
    if word in wordList:
        result = True
        for i in word:
            if i in hand_copy.keys() and hand_copy[i] != 0:
                hand_copy[i] -= 1
            else:
                result = False
                break
    return result
