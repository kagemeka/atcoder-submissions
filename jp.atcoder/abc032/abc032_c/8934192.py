import sys
from bisect import bisect_right as bi_r

n, k, *s = map(int, sys.stdin.read().split())

def main():
    cumprod = s.copy()
    for i in range(1, n):
        cumprod[i] *= cumprod[i-1]
        if cumprod[i] == 0:
            return n

    res = [None] * n
    res[0] = bi_r(cumprod, k)
    for i in range(1, n):
        res[i] = bi_r(cumprod, cumprod[i-1] * k) - i

    ans = max(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
