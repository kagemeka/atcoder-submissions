import sys

def gcd(a, b): return gcd(b, a % b) if b else abs(a)
def lcm(a, b): return abs(a // gcd(a, b) * b)

n, *a = map(int, sys.stdin.read().split())

def main():
    lg = [0] * n
    rg = [0] * n
    for i in range(1, n):
        lg[i] = gcd(lg[i-1], a[i-1])
    for i in range(n-2, -1, -1):
        rg[i] = gcd(rg[i+1], a[i+1])
    res = max([gcd(lg[i], rg[i]) for i in range(n)])
    print(res)

if __name__ ==  '__main__':
    main()
