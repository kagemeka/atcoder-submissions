import sys
from math import floor, sqrt
from collections import defaultdict

MOD = 10 ** 9 + 7

n = int(sys.stdin.readline().rstrip())

res = defaultdict(int)

def primeFactorize(n):
    while n % 2 == 0:
        res[2] += 1
        n //= 2
    if n == 1:
        return
    for i in range(3, floor(sqrt(n))+1, 2):
        while n % i == 0:
            res[i] += 1
            n //= i
        if n == 1:
            return
    res[n] += 1

def main():
    for i in range(1, n+1):
        primeFactorize(i)

    ans = 1
    for c in res.values():
        ans *= c + 1
        ans %= MOD

    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
