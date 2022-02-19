import math
import typing


def main() -> typing.NoReturn:
    x = int(input())

    t = math.ceil((2 * x + 1 / 4) ** 0.5 - 1 / 2)
    print(t)


main()
