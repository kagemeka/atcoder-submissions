# 2019-11-27 17:10:30(JST)
import sys
from math import ceil

def main():
    a, b, k, l = map(int, sys.stdin.readline().split())

    if a * l <= b:
        ans = a * k
    else:
        ans = min(k // l * b + k % l * a, ceil(k / l) * b)

    print(ans)

if __name__ == '__main__':
    main()
