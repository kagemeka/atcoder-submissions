import sys
from collections import Counter

def comb(n, r):
    if r > n:
        return 0
    r = min(r, n - r)
    if r == 0: return 1
    if r == 1: return n
    numerator = list(range(n-r+1, n+1))
    denominator = list(range(1, r+1))
    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot
    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])
    return result

n, *a = map(int, sys.stdin.read().split())

def main():
    c = Counter(a)
    res = 0
    for v in c.values():
        res += comb(v, 2)

    for i in a:
        yield res - comb(c[i], 2) + comb(c[i]-1, 2)

if __name__ == "__main__":
    ans = main()
    print(*ans, sep='\n')
