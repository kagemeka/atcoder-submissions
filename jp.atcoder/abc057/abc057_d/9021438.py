import sys
from bisect import bisect_left as bi_l, bisect_right as bi_r
import scipy.special

def comb(n, r):
    return scipy.special.comb(n, r, exact=True)

n, a, b, *v = map(int, sys.stdin.read().split())

def main():
    v.sort()

    ma = v[n-a:n]
    yield sum(ma) / a

    lo = ma[0]
    hi = ma[-1]

    res = 0
    lo_cnt = bi_r(v, lo) - bi_l(v, lo)
    if lo == hi:
        for c in range(a, min(b, lo_cnt) + 1):
            res += comb(lo_cnt, c)
    else:
        allowed_cnt = bi_r(ma, lo)
        res = comb(lo_cnt, allowed_cnt)

    yield res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
