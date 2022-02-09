import typing
import math

def main() -> typing.NoReturn:
    n = int(input())
    a = [1] * n
    for i in range(n - 1):
        a[i] *= 2
    for i in range(1, n):
        a[i] *= 3
    a[0] *= 5
    a[-1] *= 5
    k = 1 << 14
    is_prime = [True] * k
    is_prime[0] = is_prime[1] = False
    for i in range(2, k):
        if i * i > k: break
        if not is_prime[i]: continue
        for j in range(i * i, k, i):
            is_prime[j] = False

    p = 7
    x = 1
    for i in range(1, n):
        x *= p
        if x * a[i] > 10000:
            p += 1
            while not is_prime[p]: p += 1
            x = p
        a[i] *= x
    print(*a)

main()
