"""
Problem #6: Playing a game

A game consists of playing multiple hands. We need to implement one final
function to complete our word-game program. Write the code that implements
the playGame function. You should remove the code that is currently
uncommented in the playGame body. Read through the specification and make
sure you understand what this function accomplishes. For the game, you should
use the HAND_SIZE constant to determine the number of cards in a hand.
"""


def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    while True:
        answer = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if answer == 'n':
            hand = dealHand(HAND_SIZE)
            playHand(hand, wordList, HAND_SIZE)
        elif answer == 'r':
            try:
                playHand(hand, wordList, HAND_SIZE)
            except:
                print('You have not played a hand yet. Please play a new hand first!')
        elif answer == 'e':
            break
        else:
            print("Invalid command.")
            
