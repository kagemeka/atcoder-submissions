import typing
import heapq

def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    a = [list(map(lambda x: int(x) - 1, input().split()))[::-1] for _ in range(n)]

    cnt = [0] * m
    for i in range(n):
        cnt[a[i][-1]] += 1

    inf = 1 << 60
    mn = inf
    removed = set()
    for _ in range(m - 1):
        mx = max(cnt)
        mn = min(mn, mx)
        for i in range(m):
            if cnt[i] < mx: continue
            removed.add(i)
            cnt = [0] * m
            for j in range(n):
                while a[j][-1] in removed:
                    a[j].pop()
                cnt[a[j][-1]] += 1
            break
    print(mn)

main()
