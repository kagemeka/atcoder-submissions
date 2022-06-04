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
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(k):
        a[i::k] = sorted(a[i::k])

    for i in range(n - 1):
        if a[i] > a[i + 1]:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
