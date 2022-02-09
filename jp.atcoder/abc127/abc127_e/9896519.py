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
    if r > n or r < 0: return 0
    return fac[n] * ifac[r] % mod * ifac[n-r] % mod

n, m, k = map(int, sys.stdin.readline().split())

def main():
    vert = list(range(n+1))
    horiz = list(range(m+1))
    for i in range(1, n):
        vert[i+1] += vert[i]
        vert[i+1] %= MOD
    for i in range(1, m):
        horiz[i+1] += horiz[i]
        horiz[i+1] %= MOD

    res = 0
    for i in range(1, n):
        res += (vert[n] - vert[i] - i * (n - i)) * m % MOD * m % MOD
        res %= MOD
    for i in range(1, m):
        res += (horiz[m] - horiz[i] - i * (m - i)) * n % MOD * n % MOD
        res %= MOD

    res *= comb(n*m-2, k-2)
    res %= MOD
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
