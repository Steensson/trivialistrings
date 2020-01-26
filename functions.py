"""Different kinds of string trivialities."""
import re
import random


def kripkerize(string: str, lambdacism: bool = False) -> str:
    """Replace r (R) and l (L) with w (W)."""
    string = re.sub('r', 'w', string)
    string = re.sub('R', 'W', string)

    if lambdacism:
        string = re.sub('l', 'w', string)
        string = re.sub('L', 'W', string)

    return string


def margonize(string: str) -> str:
    """Randomly transform characters into lower or upper."""
    return ''.join([
        char.upper()
        if random.uniform(0, 1) < 0.5 else char
        for char in string.lower()
    ])


def rev(string: str) -> str:
    """Reverse string."""
    return string[::-1]
