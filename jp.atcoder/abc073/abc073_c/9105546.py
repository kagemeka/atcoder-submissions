import sys
from collections import Counter

n, *a = map(int, sys.stdin.read().split())

def main():
    res = 0
    for c in Counter(a).values():
        res += c & 1

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
