# 2019-11-25 22:51:53(JST)
import sys
from collections import Counter

MOD = 10 ** 9 + 7

def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    res = 1
    for c in Counter(s).values():
        res = res * (c + 1) % MOD

    res = (res - 1) % MOD

    print(res)

if __name__ == '__main__':
    main()
