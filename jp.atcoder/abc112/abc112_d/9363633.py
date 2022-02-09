import sys
from math import sqrt, floor
from bisect import bisect_right as bi_r

n, m = map(int, sys.stdin.readline().split())

def factorize(n):
    res = [1]
    for i in range(2, floor(sqrt(n)) + 1):
        if not n % i:
            res.append(i)
    return res

def main():
    res = factorize(m)
    ans = res[bi_r(res, m // n) - 1]
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
