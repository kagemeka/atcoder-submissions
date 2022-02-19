import bisect
import typing


def main() -> typing.NoReturn:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for _ in range(q):
        x = int(input())
        print(n - bisect.bisect_left(a, x))

main()
