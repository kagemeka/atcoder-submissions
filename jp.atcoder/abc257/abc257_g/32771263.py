# / mypy: ignore-errors
import typing


T = typing.TypeVar("T")


def z_algorithm(a: typing.Sequence[T]) -> typing.List[int]:
    n = len(a)
    lcp = [0] * n
    l = 0
    for i in range(1, n):
        r = l + lcp[l]
        d = 0 if r <= i else min(lcp[i - l], r - i)
        while i + d < n and a[i + d] == a[d]:
            d += 1
        lcp[i] = d
        if i + d > r:
            l = i
    lcp[0] = n
    return lcp


def main() -> None:
    s = input()
    t = input()
    max_len = z_algorithm(s + "$" + t)

    k = 0
    r = 0
    n = len(s)
    m = len(t)
    i = 0
    while r < m:
        nr = r
        while i <= r:
            nr = max(nr, i + max_len[n + 1 + i])
            i += 1
        if nr == r:
            print(-1)
            return
        r = nr
        k += 1
    print(k)


main()
