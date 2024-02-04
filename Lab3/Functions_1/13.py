import random

print("Hello! What is your name?")

name = input()

randomNumber = random.randint(1, 20)

print(f"Well, {name}, I am thinking of a number between 1 and 20\nTake a guess.")

count = 0

guess = int(input())

while guess != randomNumber:
    count += 1

    if guess > randomNumber:
        print(f"Your guess is too big\nTake a guess")
        
    else:
        print(f"Your guess is too low\nTake a guess")
    
    guess = int(input())

print(f"Good job, {name}! You guessed my number in {count} guesses")

