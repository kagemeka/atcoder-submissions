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

    s = list(map(int, input()))
    w = list(map(int, input().split()))

    indices = sorted(range(n), key=lambda i: (w[i], -s[i]))
    w = [w[i] for i in indices]
    s = [s[i] for i in indices]

    cnt = s.count(1)
    mx = cnt
    # i = 0
    # while i < n:

    #     while i
    for i in range(n):
        if s[i] == 1:
            cnt -= 1
        else:
            cnt += 1
        mx = max(mx, cnt)
    print(mx)


main()
