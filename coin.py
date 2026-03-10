"""
Program: Coin Class for Match Coins Game
Author: Damchhig Lama
Purpose: This program defines a Coin class that represents a coin
         that can be tossed and land on Heads or Tails.
Starter Code: None
Date: March 10, 2026
"""

import random


class Coin:
    """A class that represents a coin."""

    def __init__(self) -> None:
        """Initialize the coin with a starting side."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def toss(self) -> None:
        """Toss the coin and randomly change the side."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self) -> str:
        """Return the side that is currently facing up."""
        return self.__sideup
