import sys
import typing

import numba as nb
import numpy as np


@nb.njit((), cache=True)
def solve() -> typing.NoReturn:
    ...


import itertools


def main() -> typing.NoReturn:
    s = list(input())
    # a = set()
    print(len(set(itertools.permutations(s))))



main()
