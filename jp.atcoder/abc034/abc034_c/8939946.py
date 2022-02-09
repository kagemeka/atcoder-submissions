import sys

P = 10 ** 9 + 7
def make_table(n=2*10**5, p=10**9+7):
    fac = [None] * (n + 1)
    fac[0] = 1
    ifac = fac.copy()
    for i in range(1, n+1):
        fac[i] = fac[i-1] * i % p
    ifac[n] = pow(fac[n], p-2, p)
    for i in range(n-1, 0, -1):
        ifac[i] = ifac[i+1] * (i + 1) % p
    return fac, ifac

fac, ifac = make_table()

def comb(n, r, mod=10**9+7):
    if r < 0 or r > n:
        return 0
    return fac[n] * ifac[n-r] % mod * ifac[r] % mod


w, h = map(int, sys.stdin.readline().split())

def main():
    return comb(w + h - 2, h - 1)

if __name__ == '__main__':
    ans = main()
    print(ans)
