import sys
from collections import Counter

n, *a = map(int, sys.stdin.read().split())

def main():
    c = Counter(a)
    if n & 1:
        if c.get(0, 0) != 1:
            return 0
        for i in range(2, n, 2):
            if c.get(i, 0) != 2:
                return 0
    else:
        for i in range(1, n, 2):
            if c.get(i, 0) != 2:
                return 0

    return 2 ** (n // 2)

if __name__ == '__main__':
    ans = main()
    print(ans)
