import random
import math


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def get_player_choice():
    while True:
        choice = input("Choose rock(r), paper(p), or scissors(s): ").lower()
        if (choice == "r" or choice == "rock" or
            choice == "p" or choice == "paper" or
                choice == "s" or choice == "scissors"):
            if choice == "r":
                return "rock"
            elif choice == "p":
                return "paper"
            elif choice == "s":
                return "scissors"
        else:
            print(
                f"...{choice} is not a valid choice. Please try again...")
            continue


def get_rounds():
    while True:
        rounds = input(f"Choose number of rounds: ")

        if rounds.isnumeric():
            return int(rounds)
        else:
            print(f"Must choose a number!")


def rock_paper_scissors():
    # 1 - rock
    # 2 - paper
    # 3 - scissors

    rounds = get_rounds()
    winning_score = math.floor(rounds/2) + 1

    computer_choice = ""
    player_choice = ""

    computer_score = 0
    player_score = 0

    while computer_score < winning_score and player_score < winning_score and computer_score + player_score < rounds:
        while True:
            computer_choice = get_computer_choice()
            player_choice = get_player_choice()

            if computer_choice == player_choice:
                print(f"TIED! Go again...")
                continue
            else:
                break

        if (player_choice == "rock" and computer_choice == "paper" or
            player_choice == "paper" and computer_choice == "scissors" or
                player_choice == "scissors" and computer_choice == "rock"):
            computer_score += 1
            print(
                f"Computer chose {computer_choice}, which beats {player_choice}, COMPUTER scores 1 point!")
        else:
            player_score += 1
            print(
                f"Computer chose {computer_choice}, which is weak against {player_choice}, YOU score 1 point!")

    if computer_score == player_score:
        print(
            f"You and computer tied with {player_score} points. Try an odd number of rounds next time.")
    elif computer_score < player_score:
        print(
            f"You win with {player_score} points versus {computer_score} from the computer!")
    else:
        print(
            f"You lost with {player_score} points versus {computer_score} from the computer...")


rock_paper_scissors()
