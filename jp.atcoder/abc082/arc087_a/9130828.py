import sys
from collections import Counter

n, *a = map(int, sys.stdin.read().split())

def main():
    res = 0
    for v, c in Counter(a).items():
        if c < v:
            res += c
        elif c > v:
            res += c - v
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
