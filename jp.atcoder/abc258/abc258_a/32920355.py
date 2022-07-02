# / mypy: ignore-errors
import typing


def main() -> None:
    k = int(input())
    t = 60 * 21 + k
    m = t % 60
    t //= 60
    h = t % 24
    print(f"{h:02}:{m:02}")


main()
