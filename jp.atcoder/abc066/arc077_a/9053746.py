import sys
from collections import deque

n, *a = map(int, sys.stdin.read().split())

def main():
    b = deque()
    for i in range(n):
        if i & 1:
            b.appendleft(a[i])
        else:
            b.append(a[i])
    res = list(b)
    if n & 1:
        res = res[::-1]

    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
