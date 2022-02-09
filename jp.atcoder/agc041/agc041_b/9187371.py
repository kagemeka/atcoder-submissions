import sys
from bisect import bisect_right as bi_r
from heapq import heapify, heappop, heappush

n, m, v, p, *a = map(int, sys.stdin.read().split())

def main():
    a.sort()
    # return a

    for i in range(n):
        l = bi_r(a, a[i]) - 1
        r = max(0, v - l - 1)
        if r >= p:
            cand = a[l+1:n-p+1]
            ma = cand[-1]
            heapify(cand)
            remain = m * (r - (p - 1))
            while True:
                x = heappop(cand)
                if x == ma:
                    heappush(cand, x)
                    break
                d = ma - x
                if remain < d:
                    remain = 0
                    break
                remain -= d
                heappush(cand, ma)

            if not remain:
                if a[i] + m >= ma:
                    return n - i
            le = len(cand)
            ma += (remain + le - 1) // le
            if a[i] + m >= ma:
                return n - i
        else:
            if a[i] + m >= a[n-p]:
                return n - i

if __name__ == '__main__':
    ans = main()
    print(ans)
