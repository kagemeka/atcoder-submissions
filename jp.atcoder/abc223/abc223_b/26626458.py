import typing
import sys
import numpy as np
import numba as nb



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
