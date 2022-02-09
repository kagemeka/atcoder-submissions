import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

n, *a = map(int, sys.stdin.read().split())

def main():
    l_gcd = [None] * n
    r_gcd = [None] * n
    l_gcd[1] = a[0]
    r_gcd[n-2] = a[-1]

    for i in range(2, n):
        l_gcd[i] = gcd(l_gcd[i-1], a[i-1])
    for i in range(n-3, -1, -1):
        r_gcd[i] = gcd(r_gcd[i+1], a[i+1])

    res = max(r_gcd[0], l_gcd[n-1])
    for i in range(1, n-1):
        res = max(res, gcd(l_gcd[i], r_gcd[i]))
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
