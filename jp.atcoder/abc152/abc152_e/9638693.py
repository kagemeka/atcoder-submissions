import sys
from functools import reduce

MOD = 10 ** 9 + 7

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a // gcd(a, b) * b)

n, *A = map(int, sys.stdin.read().split())

def main():
    l = reduce(lcm, A, 1) % MOD

    res = 0
    for a in A:
        res += l * pow(a, MOD-2, MOD) % MOD
        res %= MOD

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
