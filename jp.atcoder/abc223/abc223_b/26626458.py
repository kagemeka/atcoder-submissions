import sys
import typing

import numba as nb
import numpy as np


def solve() -> typing.NoReturn:
    ...


def main() -> typing.NoReturn:
    s = input()
    n = len(s)
    cand = []
    for i in range(n):
        cand.append(s[i:] + s[:i])
    cand.sort()
    print(min(cand))
    print(max(cand))


main()
