import sys
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

n, X, *x = map(int, sys.stdin.read().split())

def main():
    x.append(X)
    for i in range(n):
        x[i] -= x[i+1]
    x[-1] -= X

    return reduce(gcd, x)

if __name__ == '__main__':
    ans = main()
    print(ans)
