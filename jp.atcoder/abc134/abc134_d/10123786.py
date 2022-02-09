import sys
from math import floor, sqrt

n, *a = map(int, sys.stdin.read().split())
a = [None] + a

def factorize(n):
    res = []
    for i in range(1, floor(sqrt(n)) + 1):
        if not n % i:
            res.append(i)
            res.append(n // i)
    return sorted(res)

def main():
    res = [0] * (n + 1)
    chosen = []
    for i in range(n, 0, -1):
        if a[i] ^ res[i]:
            chosen.append(i)
            facts = factorize(i)
            for j in facts:
                res[j] ^= 1

    if chosen:
        m = len(chosen)
        return [m], chosen[::-1]
    else:
        return [[0]]

if __name__ == '__main__':
    ans = main()
    for a in ans:
        print(*a, sep=' ')
