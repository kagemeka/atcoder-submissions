import sys
from functools import reduce

def gcd(a, b): return gcd(b, a % b) if b else abs(a)
def lcm(a, b): return abs(a // gcd(a, b) * b)

n, *a = map(int, sys.stdin.read().split())

def main():
    print(reduce(gcd, a))

if __name__ ==  '__main__':
    main()
