import sys

MOD = 10 ** 9 + 7

def make_table(n=10**6, p=10**9+7):
    fac = [None] * (n + 1)
    fac[0] = 1
    ifac = fac.copy()
    for i in range(1, n + 1):
        fac[i] = fac[i-1] * i % p
    ifac[n] = pow(fac[n], p - 2, p)
    for i in range(n-1, 0, -1):
        ifac[i] = ifac[i+1] * (i + 1) % p
    return fac, ifac
fac, ifac = make_table()
def comb_mod(n, r, mod=10**9+7):
    if r < 0 or r > n:
        return 0
    return fac[n] * ifac[r] % mod * ifac[n-r] % mod

h, w, a, b = map(int, sys.stdin.readline().split())

def main():
    total = comb_mod(h+w-2, h-1)

    ng = 0
    j = b - 1
    for i in range(h - a, h):
        ng += comb_mod(i + j, i) * comb_mod(h-1-i + w-1-b, h-1-i) % MOD
        ng %= MOD

    ans = (total - ng) % MOD
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
