import typing
import itertools

def main() -> typing.NoReturn:
    s, k = input().split()
    k = int(k)
    cand = sorted(set(itertools.permutations(s)))
    print(''.join(cand[k - 1]))

main()
