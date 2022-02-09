import typing
import math

def main() -> typing.NoReturn:
    a, b = map(int, input().split())

    # count of prime factors of gcd(a, b) + 1

    n = math.gcd(a, b)

    cnt = 1
    for i in range(2, n + 1):
        if i * i > n: break
        if n % i: continue
        cnt += 1
        while n % i == 0:
            n //= i
    if n > 1:
        cnt += 1
    print(cnt)

main()
