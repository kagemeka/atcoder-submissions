import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a // gcd(a, b) * b)

a, b, n = map(int, sys.stdin.read().split())

def main():
    l = lcm(a, b)
    ans = (n + l - 1) // l * l
    print(ans)

if __name__ ==  '__main__':
    main()
