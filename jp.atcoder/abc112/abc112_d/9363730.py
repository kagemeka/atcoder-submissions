import sys
from math import sqrt, floor
from bisect import bisect_right as bi_r

def factorize(n):
    res = []
    for i in range(1, floor(sqrt(n)) + 1):
        if not n % i:
            res.append(i, n // i)
    return sorted(res)

n, m = map(int, sys.stdin.readline().split())


def main():
    res = factorize(m)
    ans = res[bi_r(res, m / n) - 1]
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
