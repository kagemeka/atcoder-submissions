import itertools
import typing


def main() -> typing.NoReturn:
    s, k = input().split()
    k = int(k)
    cand = sorted(set(itertools.permutations(s)))
    print(''.join(cand[k - 1]))

main()
