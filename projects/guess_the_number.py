# Guess the number that the computer generated
import random

# Problem - add complexity to a guess the number function:
# 1) add a guess attempt counter and show it after the player succeeds
# 2) add a handler to catch non-integer inputs and ask them to try again
# 3) add an option to toggle hint after an incorrect guess to show whether subsequent guesses is too high or too low


def user_guess(x):
    hint = False
    attempts = 0
    random_number = random.randint(1, x)
    guess = 0

    while True:
        attempts += 1
        guess = input(
            f"Guess a number between 1 and {x}. Input a number or type \"hint\" to toggle hint: ")

        if guess.isnumeric():
            guess = int(guess)
        elif guess == "hint":
            hint = not hint
            display_hint = "on" if hint == True else "off"
            print(f"You have spent one guess to {display_hint} hints!")
            continue
        else:
            print(f"Oops! You must enter a number.")
            continue

        if guess == random_number:
            if attempts == 1:
                print(f"Insane! You guessed correctly on first try! ")
            else:
                print(
                    f"Congratulations, you guessed correctly after {attempts} tries! ")
            break
        else:
            if hint:
                hint_text = "low" if guess < random_number else "high"
                print(f"{guess} is too {hint_text}! Try again.")
            else:
                print(f"{guess} is incorrect! Try again.")
    return attempts


def computer_guess(x):
    low = 1
    high = x
    attempts = 0
    print(f"It's time to let the computer guess your number!")

    while True:
        attempts += 1
        computer_guess = random.randint(low, high)
        result = input(
            f"Is {computer_guess} too low(L), too high (H), or correct (C)?").lower()

        if result == "c":
            print(f"The computer guessed correct, after {attempts} attempts!")
            break
        elif result == "l":
            low = computer_guess + 1
        elif result == "h":
            high = computer_guess - 1
    return attempts


def guess_the_number():
    number = int(
        input(f"Let's play a guessing game! Pick a number to set the limit: "))

    user_attempts = user_guess(number)
    comp_attempts = computer_guess(number)

    if user_attempts < comp_attempts:
        print(
            f"Congrats! You won against the computer with {user_attempts} attempts")
    elif user_attempts > comp_attempts:
        print(
            f"You lose. The computer has beat you with {comp_attempts} attempts")
    else:
        print(f"You and the computer tied both with {user_attempts} attempts!")


guess_the_number()
