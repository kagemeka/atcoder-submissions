import typing
import itertools
import math

def main() -> typing.NoReturn:
    n = int(input())
    a = [2, 3]
    x = 4

    def is_ok(x: int) -> bool:
        return all(math.gcd(x, y) > 1 for y in a)

    for _ in range(n - 2):
        while not is_ok(x): x += 1
        a.append(x)
        x += 1
    assert a[-1] <= 10000
    print(*a)

main()
