import sys
from collections import Counter

n, *a = map(int, sys.stdin.read().split())

def main():
    cb = Counter(a[i] + i for i in range(n))
    cc = Counter(j - a[j] for j in range(n))
    tot = 0
    for v, c in cb.items():
        tot += c * cc[v]
    print(tot)

if __name__ == '__main__':
    main()
