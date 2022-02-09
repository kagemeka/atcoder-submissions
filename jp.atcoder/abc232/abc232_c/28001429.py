import typing
import itertools
import collections

def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    ab = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
    cd = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]

    ab.sort()
    for perm in itertools.permutations(range(n)):
        tmp = []
        for i, (c, d) in enumerate(cd):
            c = perm[c]
            d = perm[d]
            if c > d:
                c, d = d, c
            tmp.append((c, d))
        tmp.sort()
        if tmp == ab:
            print('Yes')
            return
    print('No')


main()
