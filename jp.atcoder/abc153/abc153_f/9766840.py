import sys
from math import ceil
from bisect import bisect_left as bi_l

n, d, a, *xh = map(int, sys.stdin.read().split())
xh = [(x, ceil(h / a)) for x, h in sorted(zip(*[iter(xh)] * 2))]

def main():
    cnt = 0
    l = 0
    r = []
    s = [0]
    tmp = 0
    i = 0
    while l < n:
        x, h = xh[l]
        j = bi_l(r, x)
        if j > i:
            tmp -= s[j]
            i = j
        if h - tmp <= 0:
            l += 1
            continue
        cnt += h - tmp
        r.append(x + d * 2)
        s.append(h - tmp)
        tmp = h
        l += 1
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
