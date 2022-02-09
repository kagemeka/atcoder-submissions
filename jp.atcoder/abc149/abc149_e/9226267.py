import sys
from itertools import accumulate
from bisect import bisect_left as bi_l, bisect_right as bisect_right

n, m, *a = map(int, sys.stdin.read().split())
a.sort()

def possible(border):
    pair_cnt = 0
    for i in range(n):
        aj = border - a[i]
        j = bi_l(a, aj)
        pair_cnt += n - j
    return pair_cnt >= m

def main():
    s = [0] + list(accumulate(a))

    lo = 1; hi = a[-1] * 2 + 1
    while lo + 1 < hi:
        border = (lo + hi) // 2
        if possible(border):
            lo = border
        else:
            hi = border
    res = lo
    ans = 0
    minimum = float('inf')
    cnt = 0
    for i in range(n):
        aj = res - a[i]
        j = bi_l(a, aj)
        ans += s[n] - s[j] + a[i] * (n - j)
        cnt += n - j
        if j < n:
            minimum = min(minimum, a[i] + a[j])

    ans -= (cnt - m) * minimum
    return ans


if __name__ == '__main__':
    ans = main()
    print(ans)
