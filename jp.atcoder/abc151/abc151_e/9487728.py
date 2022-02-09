import sys
from itertools import accumulate

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

    s1 = a.copy()
    for i in range(n-1):
        s1[i+1] += s1[i]
        s1[i+1] %= MOD
    s2 = a[::-1]
    for i in range(n-1):
        s2[i+1] += s2[i]
        s2[i+1] %= MOD

    res = 0
    for m in range(k-2, n-2+1):
        res += (s2[n-(m+1)-1] - s1[n-(m+1)-1]) % MOD * comb(m, k-2) % MOD
        res %= MOD

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
