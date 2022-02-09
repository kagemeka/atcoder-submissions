import sys
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a // gcd(a, b) * b)

n, *t = map(int, sys.stdin.read().split())

def main():
    return reduce(lcm, t)

if __name__ == '__main__':
    ans = main()
    print(ans)
