import sys
from string import digits
MOD = 10 ** 9 + 7

def main():
    n, *a = map(int, sys.stdin.read().split())

    res = 1
    rgb = [0, 0, 0]
    for i in range(n):
        cur = a[i]
        res = res * rgb.count(cur) % MOD
        if rgb[0] == cur:
            rgb[0] += 1
        elif rgb[1] == cur:
            rgb[1] += 1
        elif rgb[2] == cur:
            rgb[2] += 1

    print(res)

if __name__ == '__main__':
    main()
