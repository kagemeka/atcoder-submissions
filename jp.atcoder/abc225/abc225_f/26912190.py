import typing
import sys
# import numpy as np
# import numba as nb



# @nb.njit((), cache=True)
# def solve() -> typing.NoReturn:
#     ...



def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    s = sys.stdin.read().split()
    s.sort()
    print(''.join(s[:k]))


main()
