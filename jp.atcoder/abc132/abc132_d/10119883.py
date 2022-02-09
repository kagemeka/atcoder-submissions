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

fac, ifac = make_table(5*10**3)

def comb(n, r, mod=MOD):
    if r > n or r < 0:
        return 0
    return fac[n] * ifac[r] % mod * ifac[n-r] % mod

def H(n, r):
    return comb(n - 1 + r, r)

n, k = map(int, sys.stdin.readline().split())

def main():
    res = [None] * (k + 1)
    for i in range(1, k+1):
        if i > n - k + 1:
            for j in range(i, k+1):
                res[j] = 0
                break
        res[i] = comb(n-k+1, i) * H(i, k-i) % MOD

    return res[1:]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
