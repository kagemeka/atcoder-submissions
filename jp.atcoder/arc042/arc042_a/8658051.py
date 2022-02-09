# 2019-11-26 14:51:37(JST)
import sys
from collections import defaultdict

def main():
    n, m, *a = map(int, sys.stdin.read().split())

    remain = set(range(1, n + 1))
    res = defaultdict(int)
    for i in range(m-1, -1, -1):
        res[a[i]] = 1
        remain -= {a[i]}
    res = list(res.keys()) + sorted(remain)

    print('\n'.join(map(str, res)))

if __name__ == '__main__':
    main()
