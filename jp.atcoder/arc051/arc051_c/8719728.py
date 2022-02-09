import sys

MOD = 10 ** 9 + 7

def main():
    n, A, b, *a = map(int, sys.stdin.read().split())
    a = sorted(a)

    if A == 1:
        print(*a, sep='\n')
        sys.exit()

    while a[0] * A < a[-1] and b > 0:
        a[0] *= A
        b -= 1
        a = sorted(a)

    for i in range(n):
        a[i] %= MOD

    if b == 0:
        print(*a, sep='\n')
        sys.exit()

    q, r = divmod(b, n)
    for i in range(n):
        a[i] = a[i] * pow(A, q, MOD) % MOD
    for i in range(r):
        a[i] = a[i] * A % MOD

    res = a[r:] + a[:r]
    print(*res, sep='\n')

if __name__ == '__main__':
    main()
