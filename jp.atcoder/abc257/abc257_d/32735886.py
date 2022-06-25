# / mypy: ignore-errors
import typing


def debug(*objects: object, **kwargs: object) -> None:
    import os
    import pprint

    if os.environ.get("PYTHON_DEBUG") is None:
        return

    for obj in objects:
        pprint.pprint(obj)

    for key, obj in kwargs.items():
        print(f"{key}: ")
        pprint.pprint(obj)


def main() -> None:
    n = int(input())

    a = [tuple(map(int, input().split())) for _ in range(n)]

    inf = 1 << 60
    fr = [inf] * n
    to = [inf] * n
    for i in range(n):
        xi, yi, pi = a[i]
        for j in range(n):
            if j == i:
                continue
            xj, yj, pj = a[j]
            d = abs(xi - xj) + abs(yi - yj)
            fr[i] = min(fr[i], (d + pj - 1) // pj)
            to[i] = min(to[i], (d + pi - 1) // pi)

    # print(fr)
    # print(to)
    res = inf
    for i in range(n):
        mn = 0
        for j in range(n):
            if j == i:
                continue
            mn = max(mn, fr[j])
        mn = max(mn, to[i])
        res = min(mn, res)
    print(res)


main()
