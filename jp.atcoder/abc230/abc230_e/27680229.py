import typing



def floor_sum(n: int) -> int:
    s = 0
    k = floor_sqrt(n)
    for i in range(1, n // (k + 1) + 1):
        s += n // i
    for x in range(1, k + 1):
        s += x * (n // x - n // (x + 1))
    return s


def floor_sqrt(n: int) -> int:
    assert n >= 0
    x = 0
    while x * x <= n: x += 1
    return x - 1


def main() -> typing.NoReturn:
    n = int(input())
    print(floor_sum(n))

main()
