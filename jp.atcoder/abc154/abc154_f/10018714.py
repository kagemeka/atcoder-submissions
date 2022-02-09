import sys

MOD = 10 ** 9 + 7

def make_table(size=10**6+2, p=MOD):
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

def g(y, x):
    return comb(y+x+2, y+1) - 1

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

def main():
    ans = g(r2, c2) - (g(r1-1, c2) + g(r2, c1-1) - g(r1-1, c1-1)) % MOD
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
