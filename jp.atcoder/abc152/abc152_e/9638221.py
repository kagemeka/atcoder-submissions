import sys

MOD = 10 ** 9 + 7

from math import floor, sqrt
from bisect import bisect_right as bi_r
from collections import defaultdict

def prime_nums(n=10**6):
    sieve = set(range(2, n + 1))
    non_prime = set(range(2 * 2, n + 1, 2))
    sieve -= non_prime
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if i in sieve:
            non_prime = set(range(i * 2, n + 1, i))
            sieve -= non_prime
    return sieve

p_nums = sorted(prime_nums())

def make_inv_table(n=10**6, p=MOD):
    fac = [None] * (n + 1)
    fac[0] = 1
    for i in range(n):
        fac[i+1] = fac[i] * (i + 1) % p
    ifac = [None] * (n + 1)
    ifac[n] = pow(fac[n], p-2, p)
    for i in range(n, 0, -1):
        ifac[i-1] = ifac[i] * i % p
    inv = [None] * (n + 1)
    for i in range(1, n+1):
        inv[i] = ifac[i] * fac[i-1] % p
    return inv

inv = make_inv_table()

n, *A = map(int, sys.stdin.read().split())

def main():
    facs = defaultdict(int)
    for a in A:
        if a == 1:
            continue
        for p in p_nums[:bi_r(p_nums, sqrt(a))]:
            cnt = 0
            while not a % p:
                cnt += 1
                a //= p
            facs[p] = max(facs[p], cnt)
            if a == 1:
                break
        else:
            facs[a] = max(facs[a], 1)

    lcm = 1
    for f, c in facs.items():
        lcm *= pow(f, c, MOD)
        lcm %= MOD

    ans = 0
    for a in A:
        ans += lcm * inv[a] % MOD
        ans %= MOD
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
