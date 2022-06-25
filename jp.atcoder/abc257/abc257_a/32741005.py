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


import string


def main() -> None:
    n, x = map(int, input().split())

    s = ""
    for c in string.ascii_uppercase:
        s += c * n
    print(s[x - 1])


main()
