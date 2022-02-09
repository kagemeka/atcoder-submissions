import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r
from itertools import accumulate

n, H, *ab = map(int, sys.stdin.read().split())
a = ab[::2]
b = ab[1::2]

def main():
    a_max = max(a)
    b.sort()
    needless_cnt = bi_r(b, a_max)
    if needless_cnt == n:
        return (H + a_max - 1) // a_max

    cands = b[needless_cnt:]
    total = list(accumulate(cands[::-1]))

    needed_cnt = bi_l(total, H) + 1
    m = len(total)
    if needed_cnt <= m:
        return needed_cnt

    remain = H - total[-1]
    return m + (remain + a_max - 1) // a_max

if __name__ == '__main__':
    ans = main()
    print(ans)
