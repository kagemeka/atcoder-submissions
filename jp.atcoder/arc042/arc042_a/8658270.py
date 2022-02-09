# 2019-11-26 14:51:37(JST)
import sys
from collections import defaultdict

def main():
    n, m, *a = map(int, sys.stdin.read().split())

    no_dup = defaultdict(bool)
    for thread in reversed(a):
        no_dup[thread] = True

    res = list(no_dup.keys())
    ans = res + sorted(set(range(1, n + 1)) - set(res))
    print('\n'.join(map(str, ans)))

if __name__ == '__main__':
    main()
