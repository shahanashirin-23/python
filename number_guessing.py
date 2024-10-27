import random

lowest = 1
highest = 100
answer = random.randint(lowest,highest)
guesses = 0

print("Number Guessing Game")
print(f"Enter a number between {lowest} and {highest}")

is_running = True
while is_running:
    user_guess = input("Guess a number :")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        guesses += 1
        if user_guess < lowest or user_guess > highest:
            print("The number is out of range")
            print(f"Please Enter a number between {lowest} and {highest}")
        elif user_guess < answer:
            print("The number is too low")
        elif user_guess > answer:
            print("The number is too high")
        else:
            print(f"CORRECT!! The Answer was {answer}")
            print(f"no of guesses {guesses}")
            is_running = False
    else:
        print("Invalid Guess")
        print("Please Enter a number between 1 and 100")