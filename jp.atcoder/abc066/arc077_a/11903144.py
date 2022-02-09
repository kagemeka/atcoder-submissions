import sys
from collections import deque

n, *a = map(int, sys.stdin.read().split())

def main():
    b = deque()
    for i in range(n):
        if (i & 1): b.appendleft(a[i])
        else: b.append(a[i])
    if (n & 1): b.reverse()
    print(*b, sep=' ')

if __name__ ==  '__main__':
    main()
