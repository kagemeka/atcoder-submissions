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
    icumsum = [None] * (size + 1)
    icumsum[1] = 1
    for i in range(1, size):
        icumsum[i+1] = (icumsum[i] + fac[i] * ifac[i+1]) % MOD
    return fac, ifac, icumsum

fac, ifac, icumsum = make_table(10**5)

def comb(n, r, mod=MOD):
    if r > n or r < 0:
        return 0
    return fac[n] * ifac[r] % mod * ifac[n-r] % mod

n, *x = map(int, sys.stdin.read().split())

def main():
    d = [x[i+1] - x[i] for i in range(n-1)]

    res = 0
    for i in range(n-1):
        res += d[i] * icumsum[i+1]
        res %= MOD

    return res * fac[n-1] % MOD

if __name__ == '__main__':
    ans = main()
    print(ans)
