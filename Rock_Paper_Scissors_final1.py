import random

welcome_message = """
====================================
ROCK PAPER SCISSORS GAME
====================================
Rules:
- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock
"""
print(welcome_message)

choices = ["rock", "paper", "scissors"]

# Dictionary to convert abbreviations to full words
input_map = {
    "r": "rock",
    "rock": "rock",
    "p": "paper",
    "paper": "paper",
    "s": "scissors",
    "scissors": "scissors"
}

# Select game mode
while True:
    mode = input(
        "Choose a game mode:\n"
        "1 - Player vs Computer\n"
        "2 - Player vs Player\n"
        "Enter 1 or 2: "
    )

    if mode in ["1", "2"]:
        break

    print("Invalid choice. Please enter 1 or 2.")

player1_score = 0
player2_score = 0

while True:

    # Get Player 1 input
    while True:
        player1 = input(
            "\nPlayer 1 - Enter rock (r), paper (p), or scissors (s): "
        ).lower()

        if player1 in input_map:
            player1 = input_map[player1]
            break

        print("Invalid input. Enter rock/r, paper/p, or scissors/s.")

    # Get opponent move
    if mode == "1":
        player2 = random.choice(choices)
        print(f"\nComputer chooses: {player2}")
        player2_name = "Computer"

    else:
        print("\n" * 30)  # Hide Player 1's choice

        while True:
            player2 = input(
                "Player 2 - Enter rock (r), paper (p), or scissors (s): "
            ).lower()

            if player2 in input_map:
                player2 = input_map[player2]
                break

            print("Invalid input. Enter rock/r, paper/p, or scissors/s.")

        player2_name = "Player 2"

    # Determine winner
    if player1 == player2:
        print("\nIt's a tie!")

    elif (
        (player1 == "rock" and player2 == "scissors")
        or (player1 == "paper" and player2 == "rock")
        or (player1 == "scissors" and player2 == "paper")
    ):
        print("\nPlayer 1 wins this round!")
        player1_score += 1

    else:
        print(f"\n{player2_name} wins this round!")
        player2_score += 1

    # Display score
    print("\nCurrent Score")
    print(f"Player 1: {player1_score}")
    print(f"{player2_name}: {player2_score}")

    # Play again
    while True:
        play_again = input("\nPlay again? (yes/no): ").lower()

        if play_again in ["yes", "y"]:
            play_again = "yes"
            break
        elif play_again in ["no", "n"]:
            play_again = "no"
            break

        print("Please enter yes/y or no/n.")

    if play_again == "no":
        break

# Final score
print("""
================
FINAL SCORE
================
""")

print(f"Player 1: {player1_score}")
print(f"{player2_name}: {player2_score}")
print("Thanks for playing!")