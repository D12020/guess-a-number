import random
# Saleem A
# config
low = 1
high = 100


# helper functions
def show_start_screen():
    print("*************************")
    print("*  Guess a Number A.I!  *")
    print("*************************")

def show_credits():
    pass
    
def get_guess(current_low, current_high):
    guess = ( current_high + current_low)//2
    print("Is the number...")
    return guess


def pick_number():
    print ("Please think of a number between " + str(low) + " and " + str(high) + ".")
    print("Press 'enter' when ready.")
    useless_1 = input ()
  

def check_guess(guess):
    print(guess)
    test = input("Please tell me if my number was too high, too low, or if I guessed right.")
    print()
    if test in ["low", "higher","too low"]:
        check = 1
    if test in ["high", "lower", "too high"]:
        check = -1
    if test in ["right", "correct", "yes"]:
        check = 0
    return check
      

def show_result(guess):
    print()
    print("HAHA " + str(guess) + " was such an easy number to guess.")
    print("You'll NEVER win hahahahaha!!!")
 

def play_again():
    while True:
        print()
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            print()
            return True
        elif decision == 'n' or decision == 'no':
            print()
            print("OK loser, goodbye. Good luck on other games you'll play because you'll need it.")
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    check = -1
    
    pick_number()
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess)

        if check == -1:
            current_high = guess
         
        elif check == 1:
            current_low = guess

    show_result(guess)


# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



