import sys

MOD = 10 ** 9 + 7
N = 2 * 10 ** 5
fac = [None] * (N + 1)
fac[0] = 1
fac_inv = fac.copy()
for i in range(1, N + 1):
    fac[i] = fac[i-1] * i % MOD
fac_inv[N] = pow(fac[N], MOD - 2, MOD)
for i in range(N-1, 0, -1):
    fac_inv[i] = fac_inv[i+1] * (i + 1) % MOD

def comb_mod(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    res = fac[n] * fac_inv[r] * fac_inv[n-r]
    return res

n, k = map(int, sys.stdin.read().split())

def main():
    res = comb_mod(n + k - 1, k)
    return res % MOD

if __name__ == '__main__':
    ans = main()
    print(ans)
