"""
Program: Player Class for Match Coins Game
Author: Damchhig Lama
Purpose: This program defines a Player class. Each player has a name,
         a wallet of coins, and a coin object that they can toss.
Starter Code: None
Date: March 10, 2026
"""

from coin import Coin


class Player:
    """A class that represents a player."""

    def __init__(self, name: str) -> None:
        """Initialize the player with a name, wallet, and coin."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self) -> None:
        """Tell the player's coin to toss."""
        self.__coin.toss()

    def get_coin_side(self) -> str:
        """Return the side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self) -> None:
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self) -> None:
        """Remove one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self) -> int:
        """Return the number of coins in the player's wallet."""
        return self.__wallet

    def get_name(self) -> str:
        """Return the player's name."""
        return self.__name
