import sys
from math import ceil

n, *cap = map(int, sys.stdin.read().split())

def main():
    min_cap = min(cap)
    i = cap.index(min_cap) + 1

    res = (i - 1) + ceil(n / min_cap) + (5 - i)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
