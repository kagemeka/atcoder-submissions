import sys

MOD = 10 ** 9 + 7

n, a, b = map(int, sys.stdin.readline().split())
k = min(n, 2 * 10 ** 5)

def make_inv(size=10**6, p=MOD):
    fac = [None] * (size + 1)
    fac[0] = 1
    for i in range(size):
        fac[i+1] = fac[i] * (i + 1) % p
    ifac = [None] * (size + 1)
    ifac[size] = pow(fac[size], p-2, p)
    for i in range(size, 0, -1):
        ifac[i-1] = ifac[i] * i % p
    inv = [None] * (size + 1)
    for i in range(1, size+1):
        inv[i] = fac[i-1] * ifac[i] % MOD
    return inv

inv = make_inv(k)

def make_table(n, k, p=MOD):
    table = [None] * (k + 1)
    table[0] = 1
    for i in range(k):
        table[i+1] = table[i] * (n - i) % MOD * inv[i+1] % MOD
    return table

comb_n = make_table(n, k)

def main():
    res = pow(2, n, MOD) - comb_n[a] - comb_n[b] - 1
    return res % MOD

if __name__ == '__main__':
    ans = main()
    print(ans)
