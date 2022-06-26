# / mypy: ignore-errors
import typing


def main() -> None:
    a = list(map(int, input().split()))
    a.sort()
    z, y, x = a
    d = y - z
    dz = x - z - d
    if not 0 <= dz <= z:
        print(-1)
        return

    dx = d + 2 * dz
    if not 0 <= dx <= x:
        print(-1)
    else:
        print(x)


main()
