"""
Program that guesses a secret number using bisection search.

The user thinks of an integer between 0 (inclusive) and 100 (not inclusive).
The computer makes guesses, and the user give it input - high or low
"""

print("Please think of a number between 0 and 100!")

high = 100
low = 0

while True:
    guess = (high + low) // 2
    print("Is your secret number " + str(guess) + "?")

    # Asks user input
    print("Enter 'h' to indicate the guess is too high.", end=" ")
    print("Enter 'l' to indicate the guess is too low.", end=" ")
    user_input = input("Enter 'c' to indicate I guessed correctly. ").lower()
    
    # Check input and generate new guesses
    if user_input == "h":
        high = guess
    elif user_input == "l":
        low = guess
    elif user_input == "c":
        print("Game over. Your secret number was:", guess)
        break
    else:
        print("Sorry, I did not understand your input.")
