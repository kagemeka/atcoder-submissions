import typing

import numpy as np

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))

    cum_xor = 0
    for x in a:
        cum_xor ^= x
    sa = set(a)

    remained = n
    for x in a:
        if cum_xor ^ x in sa:
            print(x, cum_xor ^ x)
            remained -= 1
    # print(remained)
    if cum_xor in sa:
        print('Win')
        return
    print('Win' if remained & 1 else 'Lose')



main()
