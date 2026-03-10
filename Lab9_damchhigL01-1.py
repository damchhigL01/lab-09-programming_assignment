"""
Program: Match Coins Game
Author: Damchhig Lama
Purpose: This program runs a coin matching game between two players.
         Players toss coins and try to match the sides.
Starter Code: None
Date: March 10, 2026
"""

from player import Player


def main() -> None:
    """Run the Match Coins game."""

    print("--- Coin Match Game ---")

    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

    choice = input("\nDo you want to toss the coins? (y/n): ")

    while choice.lower() == "y":

        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("...It's a Match! Player 1 wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print("...No Match! Player 2 wins a coin.")

        print(f"\n{player1.get_name()} has {player1.get_wallet()} coins.")
        print(f"{player2.get_name()} has {player2.get_wallet()} coins.")

        choice = input("\nDo you want to toss the coins? (y/n): ")

    print("\n--- Final Score ---")

    p1 = player1.get_wallet()
    p2 = player2.get_wallet()

    print(f"Player 1: {p1}")
    print(f"Player 2: {p2}")

    if p1 > p2:
        print("Player 1 wins the game!")
    elif p2 > p1:
        print("Player 2 wins the game!")
    else:
        print("It's a draw!")


if __name__ == "__main__":
    main()
