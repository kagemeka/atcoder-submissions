import typing
import bisect
import itertools

def main() -> typing.NoReturn:
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    cnt = 0
    for i, j, k in itertools.combinations(l, 3):
        if i == j or j == k: continue
        if k >= i + j: continue
        cnt += 1
    print(cnt)

main()
