import bisect
import math


def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    xy = [tuple(map(int, input().split())) for _ in range(n)]

    inf = 1 << 30
    lo, hi = 0, inf

    def is_ok(r: float) -> bool:
        r2 = r**2
        lighted = [False] * n
        for j in a:
            j -= 1
            xj, yj = xy[j]
            for i in range(n):
                x, y = xy[i]
                d = (x - xj) ** 2 + (y - yj) ** 2
                if d <= r2:
                    lighted[i] = True
        return all(lighted)

    for _ in range(100):
        r = (lo + hi) / 2
        if is_ok(r):
            hi = r
        else:
            lo = r
    print(lo)


if __name__ == "__main__":
    import os

    if os.environ.get("PYTHON_DEBUG") is not None:
        from lib.py.debug import debug
    else:

        def debug(*args: object, **kwargs: object) -> None:
            pass

    main()
