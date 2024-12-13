import random
import math

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'


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
                f"\"{choice}\" is not a valid choice. Please try again...\n")
            continue


def get_rounds():
    while True:
        rounds = input(f"\nDecide the number of rounds to play (1-10): ")

        if rounds.isnumeric() and int(rounds) > 0 and int(rounds) <= 10:
            print(f"Best out of {rounds} rounds. Let the games begin!")
            return int(rounds)
        else:
            print(f"\nPlease choose a number between 1 and 10!")


def print_points(score):
    return "point" if score == 1 else "points"


def rock_paper_scissors():
    print("\nThe computer challenges you to a duel of Rock, Paper, Scissors!\nA game of pure wits and skill passed down from generations.")
    
    rounds = get_rounds()
    winning_score = math.floor(rounds/2) + 1

    computer_choice = ""
    player_choice = ""

    computer_score = 0
    player_score = 0

    while computer_score < winning_score and player_score < winning_score and computer_score + player_score < rounds:
        print(f"\nRound {computer_score + player_score + 1}")
        
        while True:
            computer_choice = get_computer_choice()
            player_choice = get_player_choice()

            if computer_choice == player_choice:
                print(f"{Colors.YELLOW}TIED{Colors.END}, the computer chose the same... Go again!\n")
                continue
            else:
                break

        if (player_choice == "rock" and computer_choice == "paper" or
            player_choice == "paper" and computer_choice == "scissors" or
                player_choice == "scissors" and computer_choice == "rock"):
            computer_score += 1
            print(
                f"The computer chose {computer_choice}, which beats {player_choice}, {Colors.RED}COMPUTER scores 1 point!{Colors.END}")
        else:
            player_score += 1
            print(
                f"The computer chose {computer_choice}, which is weak against {player_choice}, {Colors.GREEN}YOU score 1 point!{Colors.END}")

    score_unit = print_points(player_score)
    
    if computer_score == player_score:
        print(
            f"\n{Colors.YELLOW}You and computer tied with {player_score} {score_unit}{Colors.END}. Try an odd number of rounds next time.")
    elif computer_score < player_score:
        print(
            f"\n{Colors.GREEN}Congratulations! You win with {player_score} {score_unit}{Colors.END} versus {computer_score} from the computer!")
    else:
        print(
            f"\n{Colors.RED}Unfortunately, you lost with {player_score} {score_unit}{Colors.END} versus {computer_score} from the computer...")


if __name__ == "__main__":
    rock_paper_scissors()
