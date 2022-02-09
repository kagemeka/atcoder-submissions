import sys

def gcd(a, b): return gcd(b, a % b) if b else abs(a)
def lcm(a, b): return abs(a // gcd(a, b) * b)

n, *t = map(int, sys.stdin.read().split())

def main():
    res = 1
    for x in t:
        res = lcm(res, x)
    print(res)

if __name__ ==  '__main__':
    main()
