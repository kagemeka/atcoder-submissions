import sys
from scipy.special import comb

MOD = 10 ** 9 + 7
r, c, x, y, d, l = map(int, sys.stdin.read().split())

def main():
    block = (r - x + 1) * (c - y + 1)

    s = x * y # squares

    combi = comb(s, d, exact=True) % MOD * comb(s - d, l, exact=True) % MOD
    ans = block * combi % MOD
    print(ans)

if __name__ == '__main__':
    main()
