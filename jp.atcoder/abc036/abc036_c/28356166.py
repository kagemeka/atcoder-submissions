import typing
import bisect


def main() -> typing.NoReturn:
    n = int(input())
    a = [int(input()) for _ in range(n)]
    v = sorted(set(a))
    b = [bisect.bisect_left(v, x) for x in a]
    print(*b, sep='\n')

main()
