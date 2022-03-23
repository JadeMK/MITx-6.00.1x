"""
Problem #2: Update a hand by removing letters

Implement the updateHand function. Make sure this function has no side effects:
i.e., it must not mutate the hand passed in. Before pasting your function
definition here, be sure you've passed the appropriate tests in test_ps4a.py.
"""


def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = {i: hand[i] - word.count(i) for i in hand}
    return new_hand
