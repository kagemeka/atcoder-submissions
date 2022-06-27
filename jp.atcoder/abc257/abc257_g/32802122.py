# / mypy: ignore-errors
import typing


T = typing.TypeVar("T")


def morris_pratt_table(a: typing.Sequence[T]) -> typing.List[int]:
    # 0-indexed
    n = len(a)
    lb = [0] * n  # longest border
    d = 0
    for i in range(1, n):
        while d != 0 and a[d] != a[i]:
            d = lb[d - 1]
        if a[d] == a[i]:
            d += 1
        lb[i] = d
    return lb


def main() -> None:
    s = input()
    t = input()
    n, m = len(s), len(t)
    lb = morris_pratt_table(list(s + "$" + t))[n + 1 :]
    i = m
    k = 0
    while i > 0:
        d = lb[i - 1]
        if d == 0:
            print(-1)
            return
        i -= d
        k += 1
    print(k)


main()
