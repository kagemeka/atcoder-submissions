import sys
from math import log2, ceil

n, k = map(int, sys.stdin.readline().split())

def main():
    res = 0
    for i in range(1, n + 1):
        denom = 1
        while i < k:
            i *= 2
            denom *= 2
        res += 1 / denom
    res /= n
    print(res)

if __name__ ==  '__main__':
    main()
