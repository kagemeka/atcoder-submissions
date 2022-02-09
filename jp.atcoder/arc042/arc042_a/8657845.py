# 2019-11-26 14:51:37(JST)
import sys
from collections import deque

def main():
    n, m, *a = map(int, sys.stdin.read().split())

    threads = deque(range(1, n+1))
    for i in range(m):
        if a[i] != threads[0]:
            threads.remove(a[i])
            threads.appendleft(a[i])

    print('\n'.join(map(str, threads)))

if __name__ == '__main__':
    main()
