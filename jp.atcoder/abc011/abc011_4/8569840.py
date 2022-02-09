# 2019-11-23 18:41:55(JST)
import sys
from scipy.special import comb

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

    s =  remainder // 2

    ans = 0
    for i in range(s+1):
        ans += comb(n, r + i, exact=True) * comb(n - (r + i), i, exact=True) * comb(n - (r + i * 2), u + (s - i), exact=True)
        # 右 x 左 x 上(下は残りなので書かなくてもいい) に何回行くか

    ans *= (1 / 4) ** n
    print(ans)

if __name__ == '__main__':
    main()
