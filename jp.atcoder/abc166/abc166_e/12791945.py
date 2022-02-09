import sys
from collections import Counter

n, *a = map(int, sys.stdin.read().split())

def main():
    b = [a[i] + i for i in range(n)]
    c = [i - a[i] for i in range(n)]
    cb = Counter(b)
    cc = Counter(c)
    tot = 0
    for v, c in cb.items():
        tot += c * cc[v]
    print(tot)

if __name__ == '__main__':
    main()
