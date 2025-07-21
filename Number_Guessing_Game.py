# Guessing Game

import random                     # module

# Generate random number
secret = random.randint(1, 10)    # secret

# Start game
print("Guess a number between 1 and 10")   # prompt

# Loop
while True:                       # loop
    guess = int(input("Your guess: "))     # input
    if guess == secret:           # match
        print(" Correct! You win.")       # success
        break                     # exit
    elif guess < secret:          # low
        print("Too low! Try again.")       # hint
    else:                         # high
        print("Too high! Try again.")      # hint
