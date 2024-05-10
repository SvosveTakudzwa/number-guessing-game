##Number Guessing Game
import random

guesses = 0
top_of_range = input("Input your ceiling number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number greater than 0 next time around.")
        quit()
else:
    print("Please type a number next time around.")
    quit()
        
random_number = random.randint(0, top_of_range)

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time around.")
        continue
        
    if user_guess == random_number:
        print("Hooray! You guessed it right after",guesses,"quesses.")
        break
    else:
        print("You guessed it wrong.")
        continue