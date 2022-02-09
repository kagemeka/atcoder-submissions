# mathematical induction

import typing


def main() -> typing.NoReturn:
    # if N is odd, it's not possible that the game end after 2 turns.
    # let s = cumulative xor of A.
    # if s appears in A. first player is gonna win.
    # otherwize
    # if the game end after 2 turns, there is at least one pair i, j such that A_i ^ A_j = s.
    # and at most N // 2 pair.
    # thus, there is at least one person whose pair does not exist.
    # let this as i.
    # s ^ A_i is also not zero, and there is no j such that s ^ A_i ^ A_j = 0.
    # finally, first player will win if N is odd.
    # similarly, if s does not appear in A, second player can win even if first player do optimally.

    n = int(input())
    a = list(map(int, input().split()))
    s = 0
    for x in a:
        s ^= x
    if s in a or n & 1:
        print('Win')
    else:
        print('Lose')

main()
