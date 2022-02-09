import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

a, b, n = map(int, sys.stdin.read().split())

def main():
    l = lcm(a, b)
    for i in range(n, n + l):
        if i % l == 0:
            return i

if __name__ == '__main__':
    ans = main()
    print(ans)
