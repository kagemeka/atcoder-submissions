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
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    l = list(map(int, input().split()))
    
    x = [-1] * (n + 1)
    for i in range(k):
        x[a[i]] = i
    
    for i in range(q):
        j = l[i] - 1
        if a[j] == n:
            continue        
        if x[a[j] + 1] != -1:
            continue
        x[a[j] + 1] = j
        x[a[j]] = -1
        a[j] += 1
    print(*a)


main()
