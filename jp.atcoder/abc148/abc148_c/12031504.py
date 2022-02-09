import sys

def gcd(a, b): return gcd(b, a % b) if b else abs(a)
def lcm(a, b): return abs(a // gcd(a, b) * b)

a, b = map(int, sys.stdin.readline().split())

def main():
    print(lcm(a, b))

if __name__ ==  '__main__':
    main()
