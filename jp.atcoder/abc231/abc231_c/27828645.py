import typing
import bisect

def main() -> typing.NoReturn:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = []
    for _ in range(q):
        x = int(input())
        res.append(n - bisect.bisect_left(a, x))
    print(*res, sep='\n')

main()
