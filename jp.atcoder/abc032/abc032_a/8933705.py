import sys
from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

a, b, n = map(int, sys.stdin.read().split())

def main():
    l = lcm(a, b)
    for i in range(n, n + l):
        if i % l == 0:
            return i

if __name__ == '__main__':
    ans = main()
    print(ans)
