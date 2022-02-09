# 2019-11-23 18:41:55(JST)
import sys
# from scipy.special import comb


def comb(n, r):
    r = min(r, n - r)
    if r == 0: return 1
    if r == 1: return n

    numerator = list(range(n-r+1, n+1))
    denominator = list(range(1, r+1))

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def main():
    n, d, x, y = map(int, sys.stdin.read().split())
    x, y = abs(x), abs(y) # 一般性は崩れない


    if x % d != 0 or y % d != 0:
        print(0.0)
        sys.exit()

    if x + y > n * d:
        print(0.0)
        sys.exit()

    if (x + y) // d % 2 == 0:
        if n % 2 == 1:
            print(0.0)
            sys.exit()
    else:
        if n % 2 == 0:
            print(0.0)
            sys.exit()

    r, u = x // d, y // d
    remainder = n - r - u

    s = remainder // 2

    ans = 0
    # for i in range(s+1):
    #     ans += comb(n, r + i, exact=True) * (1/4)**(r+i) * comb(n - (r + i), i, exact=True) * (1/4)**i * comb(n - (r + i * 2), u + (s - i), exact=True) * (1/4)**(u+s-i) * (1/4)**(n-r-u-s-i)
    # print(ans)

    for i in range(s+1):
        ans += comb(n, r+i) / 4 ** (r+i) * comb(n - r - i, i) / 4**i * comb(n - r - i * 2, u + s - i) / 4**(u+s-i) / 4**(n-r-u-s-i)

    print(ans)

if __name__ == '__main__':
    main()
