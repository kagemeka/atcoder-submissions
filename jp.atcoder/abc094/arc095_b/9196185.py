import sys
from bisect import bisect_left as bi_l

n, *a = map(int, sys.stdin.read().split())

def main():
    a.sort()
    b = a[-1]
    c = (b + 1) // 2

    i = bi_l(a, c)
    if i == 0:
        return b, a[0]
    elif i == n - 1:
        return b, a[-2]
    else:
        res = a[i] if a[i] - c <= c - a[i-1] else a[i-1]
        return b, res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
