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

fac, ifac = make_table()

def comb(n, r, mod=MOD):
    if r > n or r < 0:
        return 0
    return fac[n] * ifac[r] % mod * ifac[n-r] % mod

from collections import defaultdict
from math import floor, sqrt
def prime_factorize(n):
    res = defaultdict(int)
    while n % 2 == 0:
        res[2] += 1
        n //= 2
    if n == 1:
        return res
    for i in range(3, floor(sqrt(n))+1, 2):
        while n % i == 0:
            res[i] += 1
            n //= i
        if n == 1:
            return res
    res[n] += 1
    return res

n, m = map(int, sys.stdin.readline().split())

def main():
    pfacts = prime_factorize(m)
    res = 1
    for v in pfacts.values():
        res *= comb(n-1+v, v)
        res %= MOD
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
