import bisect
import math


def main() -> None:
    r, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(2)]
    print(a[r - 1][c - 1])


if __name__ == "__main__":
    import os

    if os.environ.get("PYTHON_DEBUG") is not None:
        from lib.py.debug import debug
    else:

        def debug(*args: object, **kwargs: object) -> None:
            pass

    main()
