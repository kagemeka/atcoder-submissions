import sys
# from scipy.special import comb

MOD = 10 ** 9 + 7

n, k = map(int, sys.stdin.read().split())

def comb(n, r):
    r = min(r, n - r)
    if r == 0: return 1
    if r == 1: return n

    numerator = list(range(n-r+1, n+1))
    denominator = list(range(1, r+1))

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result

def main():
    res = comb(n + k - 1, k)
    return res % MOD

if __name__ == '__main__':
    ans = main()
    print(ans)
