import sys
from collections import Counter

n, k, *a = map(int, sys.stdin.read().split())

def main():
    c = Counter(a)
    res = sum(sorted(c.values())[:-k])
    print(res)

if __name__ ==  '__main__':
    main()
