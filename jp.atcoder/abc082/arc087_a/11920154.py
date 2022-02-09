import sys
from collections import Counter

n, *a = map(int, sys.stdin.read().split())

def main():
    res = 0
    for v, c in Counter(a).items():
        res += c if c < v else c - v
    print(res)

if __name__ ==  '__main__':
    main()
