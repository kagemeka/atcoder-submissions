import typing
import collections


def prime_factorize(
    n: int,
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    primes = []
    count = []

    for i in range(2, n + 1):
        if i * i > n: break
        if n % i: continue
        primes.append(i)
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
        count.append(cnt)

    if n > 1:
        primes.append(n)
        count.append(1)
    return primes, count


def main() -> typing.NoReturn:
    a, b = map(int, input().split())


    k = 1 << 20

    count = collections.Counter()

    for x in range(b + 1, a + 1):
        for p, c in zip(*prime_factorize(x)):
            count[p] += c
    cnt = 1
    MOD = 10 ** 9 + 7
    for c in count.values():
        cnt *= (c + 1)
        cnt %= MOD
    print(cnt)

main()
