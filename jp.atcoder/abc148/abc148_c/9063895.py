import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

a, b = map(int, sys.stdin.readline().split())

def main():
    ans = lcm(a, b)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
