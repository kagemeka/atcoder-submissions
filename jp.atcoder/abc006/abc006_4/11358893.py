import sys
from bisect import bisect_left as bi_l

INF = float('inf')

n, *c = map(int, sys.stdin.read().split())

def main():
    res = [INF] * n
    for x in c:
        i = bi_l(res, x)
        res[i] = x

    ans = n - bi_l(res, INF)
    print(ans)

if __name__ ==  '__main__':
    main()
