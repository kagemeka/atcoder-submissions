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
    # debug(1)
    print(int(input()) - int(input()))


if __name__ == "__main__":
    import sys
    import os

    if sys.argv[0] != "./Main.py":
        os.environ["PYTHON_DEBUG"] = "1"

    main()
