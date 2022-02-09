import typing


def floor_sum(n: int) -> int:
    r"""Floor Sum.

    1 <= n <= 10 ^ 16
    return \sum_{i=1}^{n} n // i
    """
    s = 0
    i = 1
    while i <= n:
        x = n // i
        j = n // x + 1
        s += x * (j - i)
        i = j
    return s


def floor_sum_v2(n: int) -> int:
    r"""Floor Sum.

    1 <= n <= 10 ^ 16
    return \sum_{i=1}^{n} n // i
    """
    s = 0
    k = floor_sqrt(n)
    for i in range(1, n // (k + 1) + 1):
        s += n // i
    for x in range(1, k + 1):
        s += x * (n // x - n // (x + 1))
    return s



def floor_sqrt(n: int) -> int:
    r"""Floor Sqrt."""
    assert n >= 0
    x = 0
    while x * x <= n: x += 1
    return x - 1


def main() -> typing.NoReturn:
    n = int(input())
    print(floor_sum(n))

main()
