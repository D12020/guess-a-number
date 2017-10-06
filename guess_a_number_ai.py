import random
import math

# Saleem A
# config
default_low = 1
default_high = 100



# helper functions
def show_start_screen():
    print("                                     *            ")
    print("                                    ***           ")
    print("                                   *****          ")
    print("                                 *********        ")
    print("                             *****************    ")
    print("                         *************************")
    print("                         *  Guess a Number A.I!  *")
    print("                         *************************")
    print("                             *****************    ")
    print("                                 *********        ")
    print("                                   *****          ")
    print("                                    ***           ")
    print("                                     *            ")

    
    

def show_credits():
    print()
    print("*********************************************")
    print("This awesome game was created by THE Saleem. ")
    print("********* Created on October 1,2017 *********")
    print("*********************************************")

def find_limit(current_high, current_low):
    limit = math.ceil(math.log((current_high - current_low) + 1, 2))
    return limit
    
def get_guess(current_low, current_high):
    guess = ( current_high + current_low)//2
    return guess

def decide_number(default_low,default_high):
    print()
    decide_1 = input("Hey " + str(name) + ", would you like to pick numbers for your game? ")
    decide_1 = decide_1.lower()
    if decide_1 in ["yes","y","yeah","yee","si","yep", "yes please"]:
        print()
        low = input("What would you like your lowest value to be? ")
        low = int(low)
        print()
        high = input("What would you like your highest value to be? ")
        high = int(high)
        
    else:
        print("OK, the default values will be used then.")
        print()
        low = default_low
        high = default_high

    return low,high

def pick_number (current_low, current_high):
    print()
    print (name + " please think of a number between " + str(current_low) + " and " + str(current_high) + ".")
    print("Press 'enter' when ready.")
    useless_1 = input ()
  

def check_guess(guess,tries,limit):
    print("Is the number....")
    print(str(guess) + "?")
    print("I have guessed " + str(tries) + "/" + str(limit) + " times")
    test = input("Please tell me if my number was too high, too low, or if I guessed right, " + name + ". " )
    test = test.lower()
    print()
    
    if test in ["low", "higher","too low", "l"]:
        check = 1
        return check
    if test in ["high", "lower", "too high", "h"]:
        check = -1
        return check
    if test in ["right", "correct", "yes", "y"]:
        check = 0
        return check
    else:
        print("Please eneter a valid repsponse or else I'll haunt you for the rest of your life.")
      

def show_result(guess,tries,limit):
    print()
    print("I guessed your number in only " + str(tries) + "/" + str(limit) + " tries.")
    print()
    print("HAHA " + str(guess) + " was such an easy number to guess.")
    print("You're so silly " + name + ", you'll NEVER win hahahahaha!!!")
 

def play_again(name):
    while True:
        print()
        decision = input("Would you like to play again " + name + "? (y/n) ")
        decision = decision.lower()

        if decision == 'y' or decision == 'yes':
            print()
            return True
        elif decision == 'n' or decision == 'no':
            print()
            print("OK loser, goodbye. Good luck " + name + " on other games you'll play because you'll need it.")
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play(name):
    current_low, current_high = decide_number(default_low,default_high)
    check = -1
    tries = 1

    pick_number(current_low, current_high)
    limit = find_limit(current_high,current_low)
    
    while check != 0:
        guess = get_guess(current_low, current_high)
        check = check_guess(guess,tries,limit)

        if check == -1:
            current_high = guess
         
        elif check == 1:
            current_low = guess

        tries +=1

    show_result(guess,tries,limit)


# Game starts running here
show_start_screen()

playing = True

while playing:
    name = input("Hello, welcome to Guess a Number A.I. What is your name? ")
    play(name)
    playing = play_again(name)

show_credits()



