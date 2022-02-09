import typing
import bisect

def main() -> typing.NoReturn:
    x, y, z, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()


    def possible(s: int) -> bool:
        cnt = 0
        for i in range(x):
            for j in range(y):
                cnt += z - bisect.bisect_left(c, s - a[i] - b[j])
        return cnt < k

    def binary_search() -> int:
        lo, hi = 0, 1 << 40
        while hi - lo > 1:
            s = (lo + hi) >> 1
            if possible(s):
                hi = s
            else:
                lo = s
        return lo

    s = binary_search()
    res = []
    for i in range(x):
        for j in range(y):
            for l in range(bisect.bisect_left(c, s - a[i] - b[j]), z):
                res.append(a[i] + b[j] + c[l])

    res.sort(reverse=True)
    print(*res[:k], sep='\n')

main()
