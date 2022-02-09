import sys
from collections import Counter

n, *a = map(int, sys.stdin.read().split())

def main():
    res = 0
    for v in Counter(a).values():
        res += v & 1
    print(res)

if __name__ ==  '__main__':
    main()
