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

fac, ifac = make_table(2*10**5)

def comb(n, r, mod=MOD):
    if r > n or r < 0:
        return 0
    return fac[n] * ifac[r] % mod * ifac[n-r] % mod

n, *c = map(int, sys.stdin.read().split())

def main():
    c.sort(reverse=True)
    res = 0
    # for i in range(n):
    #     cnt = 0
    #     for d in range(1, n+1):
    #         for j in range(d):
    #             cnt += comb(i, j) * comb(n-i-1, d-j-1) * (d - j) % MOD

    #     res += c[i] * cnt
    #     res %= MOD
    for i in range(n):
        res += c[i] * (i + 2)
        res %= MOD
    return res * 4 ** (n - 1) % MOD

if __name__ == '__main__':
    ans = main()
    print(ans)
