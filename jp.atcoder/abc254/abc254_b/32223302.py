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
    p = [[1] * (i + 1) for i in range(n)]
    for i in range(1, n):
        for j in range(1, i):
            p[i][j] = p[i - 1][j] + p[i - 1][j - 1]
    for row in p:
        print(*row)


if __name__ == "__main__":
    main()
