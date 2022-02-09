# 2019-11-25 16:19:29(JST)
import sys
from collections import deque

def main():
    n, s = sys.stdin.read().split()
    n = int(n)

    if n % 2 == 0:
        print(-1)
        sys.exit()

    ops = n // 2
    remainder = ops
    s = deque(list(s))
    ans = -1
    for _ in range(ops):
        l, r = s.popleft(), s.pop()
        if remainder % 3 == 1:
            if l == 'a' and r == 'c':
                pass
            else:
                break
        elif remainder % 3 == 2:
            if l == 'c' and r == 'a':
                pass
            else:
                break
        elif remainder % 3 == 0:
            if l == r == 'b':
                pass
            else:
                break
        remainder -= 1
    else:
        if s[0] == 'b':
            ans = ops

    print(ans)

if __name__ == '__main__':
    main()
