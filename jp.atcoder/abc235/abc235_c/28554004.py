import typing
import collections

def main() -> None:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))


    res = dict()
    cnt = collections.Counter()
    for i in range(n):
        x = a[i]
        cnt[x] += 1
        res[(x, cnt[x])] = i + 1

    ans = []
    for _ in range(q):
        x, k = map(int, input().split())
        ans.append(res.get((x, k), -1))

    print(*ans, sep='\n')

main()
