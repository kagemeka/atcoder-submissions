import sys
from collections import defaultdict, Counter
from math import floor, sqrt
from functools import reduce
from operator import mul

def prime_factorize_factorial(n):
    res = defaultdict(int)
    for i in range(n, 0, -1):
        while i % 2 == 0:
            res[2] += 1
            i //= 2
        if i == 1:
            continue
        for j in range(3, floor(sqrt(n))+1, 2):
            while i % j == 0:
                res[j] += 1
                i //= j
            if i == 1:
                break
        else:
            res[i] += 1
    return res

def comb(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n-r)
    upper = reduce(mul, range(n, n-r, -1), 1)
    lower = reduce(mul, range(r, 0, -1), 1)
    return upper // lower

n = int(sys.stdin.readline().rstrip())

def main():
    pcnt = prime_factorize_factorial(n)
    cnt_pcnt_atleast = [0] * 75
    for c in pcnt.values():
        if c <= 74:
            cnt_pcnt_atleast[c] += 1
        else:
            cnt_pcnt_atleast[74] += 1

    for i in range(74, 0, -1):
        cnt_pcnt_atleast[i-1] += cnt_pcnt_atleast[i]

    res = 0

    # 75
    res += cnt_pcnt_atleast[74]
    # 25 * 3
    res += cnt_pcnt_atleast[24] * (cnt_pcnt_atleast[2] - 1)
    # 15 * 5
    res += cnt_pcnt_atleast[14] * (cnt_pcnt_atleast[4] - 1)
    # 5 * 5 * 3
    res += comb(cnt_pcnt_atleast[4], 2) * (cnt_pcnt_atleast[2] - 2)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
