def debug(*objects: object, **kwargs: object) -> None:
    import os
    import pprint

    if os.environ.get("PYTHON_DEBUG") is None:
        return

    for obj in objects:
        pprint.pprint(obj)

    for key, obj in kwargs.items():
        print(f"{key}: ")
        pprint.pprint(obj)


import typing


def prime_factorize(n: int) -> typing.List[typing.Tuple[int, int]]:
    primes: typing.List[int] = []
    counts: typing.List[int] = []
    i = 1
    while i * i < n:
        i += 1
        if n % i:
            continue
        primes.append(i)
        counts.append(0)
        while n % i == 0:
            n //= i
            counts[-1] += 1
    if n > 1:
        primes.append(n)
        counts.append(1)
    return list(zip(primes, counts))


def main() -> None:
    n = int(input())

    cnt = 0

    for i in range(1, n + 1):
        factors = prime_factorize(i)
        x = 1
        for p, e in factors:
            if e & 1:
                x *= p
        for y in range(1, n + 1):
            if y * y * x > n:
                break
            cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
