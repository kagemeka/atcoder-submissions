import sys
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

n, *a = map(int, sys.stdin.read().split())

def main():
    return reduce(gcd, a)

if __name__ == '__main__':
    ans = main()
    print(ans)
