def main() -> None:
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    b = [int(input()) for _ in range(q)]

    c = []
    for i in range(n):
        c.append((a[i], 0, i))
    for i in range(q):
        c.append((b[i], 1, i))
    c.sort()

    res = [None] * q
    sl = 0
    cl = 0
    sr = sum(a)
    for v, j, i in c:
        if j == 0:
            sl += v
            sr -= v
            cl += 1
            continue
        res[i] = cl * v - sl + sr - (n - cl) * v
    print(*res, sep="\n")


if __name__ == "__main__":
    import os

    if os.environ.get("PYTHON_DEBUG") is not None:
        from lib.py.debug import debug
    else:

        def debug(*args: object, **kwargs: object) -> None:
            pass

    main()
