def main() -> None:
    x, a, d, n = map(int, input().split())

    mn = a
    mx = a + d * (n - 1)
    if mn > mx:
        mn, mx = mx, mn

    if d == 0:
        print(abs(a - x))
        return
    if x < mn:
        print(mn - x)
    elif x > mx:
        print(x - mx)
    else:
        if d < 0:
            d = -d
        cand = []
        for y in range(-d, d + 1):
            if (x + y - a) % d == 0:
                cand.append(y)
        res = min(abs(y) for y in cand)
        print(res)
        return


if __name__ == "__main__":
    import os

    if os.environ.get("PYTHON_DEBUG") is not None:
        from lib.py.debug import debug
    else:

        def debug(*args: object, **kwargs: object) -> None:
            pass

    main()
