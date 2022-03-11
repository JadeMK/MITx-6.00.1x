"""
you will implement the function hangman, which takes one parameter -
the secretWord the user is to guess. This starts up an interactive game of
Hangman between the user and the computer. Be sure you take advantage of the
three helper functions, isWordGuessed, getGuessedWord, and getAvailableLetters,
that you've defined in the previous part.
"""


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!\nI am thinking of a word that is", len(secretWord), "letters long.")
    guess_left = 8
    lettersGuessed = []
    # Continue guessing until the number of guesses runs out or the user wins
    while guess_left > 0 and not isWordGuessed(secretWord, lettersGuessed):
        print("-----------\nYou have", guess_left, "guesses left.")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        user_guess = input("Please guess a letter: ")
        
        # Check if the user guessed a correct character
        if user_guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", end=" ")
        elif user_guess in secretWord:
            print("Good guess:", end=" ")
        else:
            print("Oops! That letter is not in my word:", end=" ")
            guess_left -= 1
        lettersGuessed.append(user_guess)
        print(getGuessedWord(secretWord, lettersGuessed))
        
    # End the game
    print("-----------")
    if isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was " + secretWord + ".")

