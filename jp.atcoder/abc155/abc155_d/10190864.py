import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r

n, k, *a = map(int, sys.stdin.read().split())
a.sort()

def count(border):
    cnt = 0

    for i in range(n-1):
        l = a[i]
        if l == 0:
            if border >= 0:
                cnt += n - (i + 1)
        else:
            b = border / l
            if l < 0:
                j = bi_l(a, b)
                cnt += n - max(i+1, j)
            else:
                j = bi_r(a, b)
                cnt += max(j-(i+1), 0)
    return cnt

def main():
    lo = -10 ** 18 - 1
    hi = 10 ** 18 + 1
    while lo + 1 < hi:
        border = (lo + hi) // 2
        if count(border) >= k:
            hi = border
        else:
            lo = border
    return hi

if __name__ == '__main__':
    ans = main()
    print(ans)
