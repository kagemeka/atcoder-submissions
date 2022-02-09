import sys

MOD = 10 ** 9 + 7

def make_factorial_mod(n, mod):
    fac = [None] * (n + 1)
    fac[0] = 1
    for i in range(n):
        fac[i+1] = fac[i] * (i + 1) % mod
    return fac

fac = make_factorial_mod(10**5, MOD)

n, m = map(int, sys.stdin.readline().split())
if n < m:
    n, m = m, n

def main():

    if n == m:
        return fac[n] * fac[m] * 2 % MOD
    elif n == m + 1:
        return fac[n] * fac[m] % MOD
    else:
        return 0

if __name__ == '__main__':
    ans = main()
    print(ans)
