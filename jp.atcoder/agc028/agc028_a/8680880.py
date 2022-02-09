# 2019-11-28 02:28:10(JST)
import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def main():
    n, m = map(int, sys.stdin.readline().split())
    s, t = sys.stdin.read().split()

    g = gcd(n, m)
    l = lcm(n, m)

    if g == 1:
        if s[0] == t[0]:
            ans = l
        else:
            ans = -1
    else:
        for i in range(g):
            if s[i * n // g] == t[i * m // g]:
                continue
            else:
                ans = -1
                break
        else:
            ans = l

    print(ans)

if __name__ == '__main__':
    main()
