import random
#config
low = 1
high = 100
limit = 10

# start game
rand = random.randint(low,high)
print("I'm thinking of a number from " + str(low) + " to " + str(high)+ ".");

guess = -1
tries = 0

# helper functions
def get_guess():
    while True:
        g = input(" Take a guess:")

        if g.isnumeric():
            g = int(g)
            return g
        else:
            print("You must enter a number, silly.")


# play the game
while guess != rand and tries < limit:
    guess = get_guess()
 
    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries += 1
   

# tell player outcome
if guess == rand:
    print("You Win!!!!")
else:
    print ("You lose. I was thinking of the number" + str(rand) + ".")
    
print("Game over")
