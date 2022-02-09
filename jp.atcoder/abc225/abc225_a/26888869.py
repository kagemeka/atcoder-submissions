import typing
import sys
import numpy as np
import numba as nb



@nb.njit((), cache=True)
def solve() -> typing.NoReturn:
    ...


import itertools
def main() -> typing.NoReturn:
    s = list(input())
    # a = set()
    print(len(set(itertools.permutations(s))))



main()
