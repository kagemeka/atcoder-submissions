# mypy: ignore-errors

import sys

sys.setrecursionlimit(10**6)


def main() -> None:
    print(1 << int(input()))


if __name__ == "__main__":
    main()
