from sys import stdin

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)


n, *t = map(int, stdin.read().split())

a = t[0]
for i in range(1, n):
    b = t[i]
    a = lcm(a, b)

print(a)
