import random
import math

# config
low = 1
high = 10
limit = math.ceil(math.log((high - low) + 1,2))

# helper functions
def show_start_screen():
    print("**************************")
    print("*                        *")
    print("**************************")
    print("**** Guess a Number ! ****")
    print("**************************")
    print("*                        *")
    print("**************************")

def show_credits():
    print("OK, see ya later alligator. This awesome game was created by THE Saleem Alnawasreh.")
    print()
    print("Executive Producer Dick Wolf")
    
def get_guess():
    while True:
        guess = input("Guess a number: ")

        if guess.isnumeric():
            guess = int(guess)
            return guess
        else:
            print("You must enter a number silly goose.")

def pick_number():
    print("I'm thinking of a number from " + str(low) + " to " + str(high) +".")
    print("You'll only have " + str(limit) + " attempts to try and figure out my number. Good Luck!")
    print()

    return random.randint(low, high)

def check_guess(guess, rand):
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

def show_result(guess, rand):
    if guess == rand:
        print("You win!")
    else:
        print("You are such a loser! The number was " + str(rand) + ".")
        print()

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes' or decision == 'yeah' or decision == 'yep' or decision == 'yee' or decision == 'si':
            return True
        elif decision == 'n' or decision == 'no' or decision == 'nah' or decision == 'yeet' or decision == 'nope':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    guess = -1
    tries = 0

    rand = pick_number()
    
    while guess != rand and tries < limit:
        guess = get_guess()
        check_guess(guess, rand)

        tries += 1

    show_result(guess, rand)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()
