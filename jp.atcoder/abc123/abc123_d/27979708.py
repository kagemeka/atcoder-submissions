import typing
import bisect
import heapq


def main() -> typing.NoReturn:
    x, y, z, K = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    c.sort(reverse=True)
    hq = [(-(a[0] + b[0] + c[0]), 0, 0, 0)]
    res = []
    cache = set()
    for _ in range(K):
        s, i, j, k = heapq.heappop(hq)
        s *= -1
        res.append(s)
        if i + 1 < x and not (i + 1, j, k) in cache:
            heapq.heappush(hq, (-(s - a[i] + a[i + 1]), i + 1, j, k))
            cache.add((i + 1, j, k))
        if j + 1 < y and not (i, j + 1, k) in cache:
            heapq.heappush(hq, (-(s - b[j] + b[j + 1]), i, j + 1, k))
            cache.add((i, j + 1, k))
        if k + 1 < z and not (i, j, k + 1) in cache:
            heapq.heappush(hq, (-(s - c[k] + c[k + 1]), i, j, k + 1))
            cache.add((i, j, k + 1))
    print(*res, sep='\n')



main()
