# Guessing any number between 1 and 100.
# Only have 10 times to guess
import random
times=10
secret = random.randint(1,100)
print('Please Guess a Number between 1 and 100 Here:')
guess = 0
while guess != secret and times>0:
    temp = input ("")
    guess = int(temp)
    guess = int(temp)
    times = times -1
    if guess == secret:
            print("Wow, Lucky Guess!")
    else:
        if guess < secret:
            print("Your numner is Less")
        else:
            print ("Your number is Greater!")
print ("Game Over!" + "The number is " + str(secret))

