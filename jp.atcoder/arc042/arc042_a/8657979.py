# 2019-11-26 14:51:37(JST)
import sys
from collections import deque

def main():
    n, m, *a = map(int, sys.stdin.read().split())

    remain = deque(range(1, n + 1))
    res = []
    for i in range(m-1, -1, -1):
        if not a[i] in res:
            res.append(a[i])
            remain.remove(a[i])
    res += list(remain)

    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    main()
