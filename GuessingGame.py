import random

print("Welcome to the Number Guessing Game!")
print("Try to guess the number between 1-100.")

number = random.randint(1, 100)

max_attempts = 7
attempts = 0

while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1

    if guess == number:
        print("Correct! You guessed the number.")
        break

    elif guess > number:
        print("Too high!")

    else:
        print("Too low!")

else:
    print("Game over!")
    print("The number was:", number)