"""
Problem #1: Scoring a word

The first step is to implement some code that allows us to calculate the score
for a single word. The function getWordScore should accept as input a string of
lowercase letters (a word) and return the integer score for that word, using
the game's scoring rules.
"""


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    result = 0
    for i in word:
        result += SCRABBLE_LETTER_VALUES[i]
    result = result * len(word) + (50 * (len(word) == n))
    return result
