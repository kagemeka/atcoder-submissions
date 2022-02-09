# 2019-11-24 20:41:45(JST)
import sys
from collections import deque

def main():
    n, *b = map(int, sys.stdin.read().split())
    b = [None] + b

    for i in range(1, n+1):
        if b[i] > i:
            print(-1)
            exit()

    res = deque()
    while len(b) > 1:
        for i in range(len(b)-1, 0, -1):
            if b[i] == i:
                res.appendleft(b.pop(i))
                break

    print('\n'.join(map(str, res)))

if __name__ == '__main__':
    main()
