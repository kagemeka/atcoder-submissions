import sys
from itertools import accumulate

n, m = map(int, sys.stdin.readline().split())
lrs = map(int, sys.stdin.read().split())
lrs = zip(lrs, lrs, lrs)

def main():
    res = [0] * (m + 2)
    total = 0
    for l, r, s in lrs:
        res[l] += s
        res[r+1] -= s
        total += s

    *res, = accumulate(res)
    ans = total - min(res[1:-1])
    return ans

if __name__=='__main__':
    ans = main()
    print(ans)
