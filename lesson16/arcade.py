import sys
from rps import rps
from guess_number import guess_number


# TODO Create more games to add to the arcade to help apply learned information
def run_arcade(name="PlayerOne"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade menu.")

        player_choice = input(
            '\nPlease choose a game:\n1 - Guess My Number\n2 - Rock Paper Scissors\n\nOr press"x" to exit the Arcade\n\n'
        )

        if player_choice not in ["1", "2", "x"]:
            print(f"\n{name}, please enter 1, 2, or x.")
            return run_arcade(name)

        welcome_back = True

        if player_choice == "1":
            guess_my_number = guess_number(name)
            guess_my_number()
        elif player_choice == "2":
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        else:
            print("\nSee you later, Earth Astronaut.\n")
            sys.exit(f"Bye, {name}! 👋")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized arcade experience."
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person visiting the arcade.",
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")
    run_arcade(args.name)
