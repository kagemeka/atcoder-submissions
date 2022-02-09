import sys

MOD = 10 ** 9 + 7

def make_table(size=10**6, p=MOD):
    fac = [None] * (size + 1)
    fac[0] = 1
    for i in range(size):
        fac[i+1] = fac[i] * (i + 1) % p
    ifac = [None] * (size + 1)
    ifac[size] = pow(fac[size], p-2, p)
    for i in range(size, 0, -1):
        ifac[i-1] = ifac[i] * i % p
    return fac, ifac

fac, ifac = make_table(10**5)

def comb(n, r, mod=MOD):
    if r > n or r < 0:
        return 0
    return fac[n] * ifac[r] % mod * ifac[n-r] % mod

n, k, *a = map(int, sys.stdin.read().split())
a.sort()

def main():
    if k == 1:
        return 0

    ma = 0
    mi = 0
    for i in range(n):
        ma += a[i] * comb(i, k-1) % MOD
        ma %= MOD
        mi += a[i] * comb(n-1-i, k-1) % MOD
        mi %= MOD

    return (ma - mi) % MOD

if __name__ == '__main__':
    ans = main()
    print(ans)
