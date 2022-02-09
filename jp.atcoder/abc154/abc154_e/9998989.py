import sys

def comb(n, r):
    if r > n or r < 0: return 0
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

n, k = map(int, sys.stdin.read().split())

def solve(n, k):
    p = int(str(n)[0])
    l = len(str(n))

    if k == 1:
        return 9 * (l - 1) + p

    elif k == 2:
        res = 0
        for i in range(1, l-1):
            res += comb(i, 1) * 9 * 9
        res += comb(l-1, 1) * 9 * (p - 1)
        res += solve(int(str(n)[1:]), 1)
        return res

    elif k == 3:
        res = 0
        for i in range(2, l-1):
            res += comb(i, 2) * 9 ** 2 * 9
        res += comb(l-1, 2) * 9 ** 2 * (p - 1)
        res += solve(int(str(n)[1:]), 2)
        return res

def main():
    return solve(n, k)

if __name__ == '__main__':
    ans = main()
    print(ans)
