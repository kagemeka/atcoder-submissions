# mypy: ignore-errors

import sys

sys.setrecursionlimit(10**6)


def main() -> None:
    # reverse smallest in each cycle
    n = int(input())
    a = list(map(int, input().split()))

    a.reverse()
    for i in range(n - 1):
        a[i + 1] += a[i]

    print(len([x for x in a if x >= 4]))


if __name__ == "__main__":
    main()
