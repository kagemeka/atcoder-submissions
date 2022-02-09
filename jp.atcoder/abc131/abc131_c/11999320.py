import sys

def gcd(a, b): return gcd(b, a % b) if b else abs(a)
def lcm(a, b): return abs(a // gcd(a, b) * b)

a, b, c, d = map(int, sys.stdin.readline().split())

def count(n):
    return n - (n // c + n // d - n // lcm(c, d))

def main():
    print(count(b) - count(a-1))

if __name__ ==  '__main__':
    main()
