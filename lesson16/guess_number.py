import sys
import random
from enum import Enum


def guess_number(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        player_choice = input(
            f"\n{name}, I chose a number, it is 1, 2, or 3. Guess what I chose:\n1,\n2,\n3:\n\n"
        )
        if player_choice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_guess_number()

        player = int(player_choice)

        computer_choice = random.choice("123")

        computer = int(computer_choice)

        print(f"\n{name}, you chose  {player}.")
        print(f"Python chose {computer}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == computer:
                player_wins += 1
                return f"🎉 {name}, you guessed right!"
            else:
                python_wins += 1
                return f"🐍 Python wins!\n Sorry, {name}...😞"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {player_wins / game_count:.2%}")

        print(f"\nPlay again, {name}?")

        while True:
            play_again = input("\nY for Yes or \nQ to Quit\n")
            if play_again.lower() not in ["y", "q"]:
                continue
            else:
                break
        if play_again.lower() == "y":
            return play_guess_number()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Bye, {name}! 👋")
            else:
                return

    return play_guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game.",
    )

    args = parser.parse_args()

    # Making rps a module
    guess_my_number = guess_number(args.name)
    guess_my_number()
