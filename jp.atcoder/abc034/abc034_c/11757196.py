import sys

MOD = 10 ** 9 + 7

def make_fac_ifac(n=10 ** 6, p=MOD):
    fac = [None] * (n + 1)
    fac[0] = 1
    for i in range(n): fac[i+1] = fac[i] * (i + 1) % p
    ifac = [None] * (n + 1)
    ifac[n] = pow(fac[n], p - 2, p)
    for i in range(n, 0, -1): ifac[i-1] = ifac[i] * i % p
    return fac, ifac

fac, ifac = make_fac_ifac()

def mod_choose(n, r, p=MOD):
    if r > n or r < 0: return 0
    return fac[n] * ifac[r] % p * ifac[n-r] % p

h, w = map(int, sys.stdin.readline().split())

def main():
    print(mod_choose(h + w - 2, h - 1))

if __name__ ==  '__main__':
    main()
