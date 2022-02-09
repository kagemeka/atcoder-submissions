import sys
from math import sqrt, floor
from bisect import bisect_right as bi_r

n, m = map(int, sys.stdin.readline().split())

def main():
    res = [i for i in range(1, floor(sqrt(m))+1) if not m % i]
    ans = res[bi_r(res, m // n) - 1]
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
