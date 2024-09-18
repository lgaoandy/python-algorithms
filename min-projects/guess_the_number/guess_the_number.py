# Guess the number that the computer generated
import random

# Problem - add complexity to a guess the number function:
# 1) add a guess attempt counter and show it after the player succeeds
# 2) add a handler to catch non-integer inputs and ask them to try again
# 3) add an option to toggle hint after an incorrect guess to show whether subsequent guesses is too high or too low

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


def user_guess(x):
    hint = False
    attempts = 0
    random_number = random.randint(1, x)
    guess = 0

    while True:
        attempts += 1
        print(f"\nGuess {attempts}")
        guess = input(
            f"Enter a number between 1 and {x} or type \"hint\" to toggle hint: ")

        if guess.isnumeric():
            guess = int(guess)
        elif guess == "hint":
            hint = not hint
            display_hint = "on" if hint == True else "off"
            print(f"You have spent one guess to turn {display_hint} hints!")
            continue
        else:
            print(f"Oops! You must enter a number.")
            continue

        if guess == random_number:
            if attempts == 1:
                print(f"Insane! You guessed correctly on first try! ")
            else:
                print(
                    f"{Colors.GREEN}{random_number} is correct! You got it in {attempts} tries!{Colors.END}")
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
    print("\nNow it's my turn to guess!")
    input(f"Think of a number between 1 and {x}, then hit ENTER when you're ready.")

    while low <= high:
        attempts += 1
        computer_guess = random.randint(low, high)
        result = input(
            f"\nI guess {computer_guess}\nIs it too low(L), too high(H), or correct(C)?").lower()

        if result == "c":
            print(f"The computer guessed correct, after {attempts} attempts!")
            return attempts
        elif result == "l":
            low = computer_guess + 1
        elif result == "h":
            high = computer_guess - 1
    return -1


def guess_the_number():
    print("\nThe computer challenges you to a guessing game!")
    
    limit = int(input(f"Pick a number to set the limit: "))

    user_attempts = user_guess(limit)
    comp_attempts = computer_guess(limit)

    if comp_attempts == -1:
        print(
            f"\n{Colors.RED}You cheated! GAME OVER!{Colors.END}")
    elif user_attempts < comp_attempts:
        print(
            f"\n{Colors.GREEN}Congrats! You won against me with {user_attempts} attempts!{Colors.END}")
    elif user_attempts > comp_attempts:
        print(
            f"\n{Colors.RED}You lose! I have beat you with {comp_attempts} attempts!{Colors.END}")
    else:
        print(f"\n{Colors.YELLOW}You and me have tied with {user_attempts} attempts!{Colors.END}")


guess_the_number()
