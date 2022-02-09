import sys
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a // gcd(a, b) * b)

n, m, *a = map(int, sys.stdin.read().split())

def main():
    for i in range(n):
        a[i] //= 2
    l = reduce(lcm, a)

    return m // l - m // (l * 2)

if __name__ == '__main__':
    ans = main()
    print(ans)
