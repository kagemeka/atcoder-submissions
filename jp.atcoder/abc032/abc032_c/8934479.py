import sys
from bisect import bisect_right as bi_r

n, k, *s = map(int, sys.stdin.read().split())

def main():
    if 0 in s:
        return n

    # cumprod = s.copy()
    # for i in range(1, n):
    #     cumprod[i] *= cumprod[i-1]

    # res = [None] * n
    # res[0] = bi_r(cumprod, k)
    # for i in range(1, n):
    #     res[i] = bi_r(cumprod, cumprod[i-1] * k) - i

    # ans = max(res)
    # return ans

    res = [0] * n
    l = 0
    r = 0
    cumprod = s[0]
    while True:
        if cumprod <= k:
            res[l] = r - l + 1
            r += 1
            if r == n :
                break
            cumprod *= s[r]
        else:
            res[l] = r - l
            cumprod //= s[l]
            l += 1
            if l > r:
                r += 1
                if r == n:
                    break
                cumprod *= s[r]

    ans = max(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
