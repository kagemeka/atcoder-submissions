import sys
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a // gcd(a, b) * b)

def cnt_2(n):
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    return cnt

n, m, *a = map(int, sys.stdin.read().split())

def main():
    for i in range(n):
        a[i] //= 2

    cnt = cnt_2(a[0])
    for i in range(1, n):
        if cnt_2(a[i]) != cnt:
            return 0

    l = reduce(lcm, a, a[0]) * 2 ** cnt

    return m // l - m // (l * 2)

if __name__ == '__main__':
    ans = main()
    print(ans)
