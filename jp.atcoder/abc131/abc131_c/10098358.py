import sys

a, b, c, d = map(int, sys.stdin.readline().split())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a // gcd(a, b) * b)

def f(n, a, b):
    return n - (n // a + n // b - n // (lcm(a, b)))

def main():
    ans = f(b, c, d) - f(a-1, c, d)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
