# -*- coding: utf-8 -*-

"""Documentation file app.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from typing import Text

import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format

# =============================================================================
# FUNCTIONS
# =============================================================================

def binary_to_decimal(number: Text) -> int:
    if isinstance(number, str):
        return sum([pow(2, index) for index, elemento in enumerate(number[::-1]) if elemento == "1"])
    else:
        raise TypeError(f"We need a string value not {type(number)}...")

# =============================================================================
# GLOBAL DEFINITION
# =============================================================================

if __name__ == "__main__":

    cprint(figlet_format("Bin-Dic", font="starwars"), "red", "on_yellow", attrs=["dark"])

    while True:

        binary_number = input("\nDigite seu binário: ").strip(" ")

        filter_digits = list(filter(lambda x: x != "0" and x != "1", binary_number))

        if filter_digits:
            raise ValueError(f"He have digits different than 1 or 0 - {filter_digits}.")

        print(f"\nO valor decimal do binário {binary_number} é {binary_to_decimal(binary_number)}\n")

        next = input("Você quer continuar? <s> SIM - <n> NÃO: ").lower()

        if next == "n":
            print("\nSaindo...\n")
            break
