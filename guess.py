import random

def number_guessing_game():
    print("Do you wanna play number guessing game?")
    
    # Set the range
    lower_limit = 1
    upper_limit = 100
    number_to_guess = random.randint(lower_limit, upper_limit)
    
    print(f"I'm thinking of a number between {lower_limit} and {upper_limit}.")
    print("You have 3 attempts to guess it correctly!")

    attempts = 3
    while attempts > 0:
        try:
            # Get user input
            guess = int(input("Enter your guess: "))
            
            # Check the guess
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                print("Congratulations! You guessed the correct number.")
                break
            
            attempts -= 1
            if attempts > 0:
                print(f"You have {attempts} attempts left. Try again!")
            else:
                print("Sorry, you've run out of attempts!")
                print(f"The number was {number_to_guess}. Better luck next time!")
        except ValueError:
            print("Please enter a valid number.")
        
# Run the game
number_guessing_game()