
import random

def number_guessing_game():
    number = random.randint(0,20)
    guesses = 0
    while True:
        guess = int(input("Guess a number between 0 and 20: "))
        guesses += 1

        if guesses==number:
            print(f'CONGRATULATIONS!You guessed the correct number in {guesses} guesses!')
            break

        elif guess < number:
            print("Go higher!")

        else:
            print("GO lower!")
number_guessing_game()
