import sys
from math import sqrt, floor

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

a, b, k = map(int, sys.stdin.readline().split())

def main():
    g = gcd(a, b)
    cand = []
    for i in range(1, floor(sqrt(g)) + 1):
        if not g % i:
            cand.append(i)
            cand.append(g // i)
    cand.sort()
    return cand[-k]

if __name__ == '__main__':
    ans = main()
    print(ans)
