import sys
from collections import Counter

def comb(n):
    return n * (n - 1) // 2

n, *a = map(int, sys.stdin.read().split())

def main():
    c = Counter(a)
    res = 0
    for v in c.values():
        res += comb(v)

    for i in a:
        yield res - comb(c[i]) + comb(c[i]-1)

if __name__ == "__main__":
    ans = main()
    print(*ans, sep='\n')
