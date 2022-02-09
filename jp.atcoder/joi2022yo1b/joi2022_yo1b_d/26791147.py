import typing
import collections

def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))

    v, cnt = -1, 1 << 20
    for x, c in collections.Counter(a).items():
        if c > cnt: continue
        if c < cnt or x < v:
            v, cnt = x, c
    print(v)

main()
