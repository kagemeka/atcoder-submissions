import sys

def gcd(a, b): return gcd(b, a % b) if b else abs(a)
def lcm(a, b): return abs(a // gcd(a, b) * b)

n, *x = map(int, sys.stdin.read().split())

def main():
    d = abs(x[1] - x[0])
    for i in range(1, n):
        d = gcd(d, x[i+1] - x[i])
    print(d)

if __name__ ==  '__main__':
    main()
