import typing


def find_divisors(n: int) -> typing.List[int]:
    divisors = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        divisors.append(i)
        if i * i != n:
            divisors.append(n // i)
    return sorted(divisors)


def find_divisors(n: int) -> typing.List[int]:
    divisors = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i:
            continue
        divisors.append(i)
        if i * i != n:
            divisors.append(n // i)
    divisors.sort()
    return divisors


def extended_euclidean_mod(mod: int, n: int) -> typing.Tuple[int, int]:
    a, b = n % mod, mod
    x00, x01 = 1, 0
    while b:
        q, r = divmod(a, b)
        x00, x01 = x01, x00 - q * x01
        a, b = b, r
    if x00 < 0:
        x00 += mod // a
    assert 0 <= x00 < mod // a
    return a, x00


def crt_2(
    mod_0: int,
    rem_0: int,
    mod_1: int,
    rem_1: int,
) -> typing.Optional[typing.Tuple[int, int]]:
    assert 0 <= rem_0 < mod_0 > 1 and 0 <= rem_1 < mod_1 > 1
    gcd, inv_u0 = extended_euclidean_mod(mod_1, mod_0)
    if (rem_1 - rem_0) % gcd:
        return None
    u1 = mod_1 // gcd
    x = ((rem_1 - rem_0) // gcd) % u1 * inv_u0 % u1
    return mod_0 * u1, rem_0 + x * mod_0


def crt(
    pairs: typing.List[typing.Tuple[int, int]],
) -> typing.Optional[typing.Tuple[int, int]]:
    pairs = [pair for pair in pairs if pair != (1, 0)]
    assert len(pairs) >= 1
    mod, rem = pairs[0]
    assert 0 <= rem < mod > 1
    for m, r in pairs[1:]:
        assert 0 <= r < m > 1
        result = crt_2(mod, rem, m, r)
        if result is None:
            return None
        mod, rem = result
    return mod, rem


def main() -> None:
    n = int(input())
    # (k + 1)k/2 = 0 (mod N)
    # (k + 1)k = 0 (mod 2N)
    # k + 1 = 0 (mod a) and k = 0 (mod 2N/a) (for fixed a)
    # k = -1 = a - 1 (mod a) and k = 0 (mod 2N/a)
    # find k by chinese remainder theorem

    def find_k(a: int) -> typing.Optional[int]:
        pairs = [(a, a - 1), (2 * n // a, 0)]
        result = crt(pairs)
        if result is None:
            return None
        lcm, rem = result
        return rem if rem > 0 else lcm

    mn = 1 << 60
    for a in find_divisors(2 * n):
        k = find_k(a)
        if k is None:
            continue
        mn = min(mn, k)
    print(mn)


if __name__ == "__main__":
    main()
