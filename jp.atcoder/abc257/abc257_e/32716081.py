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
    cost = list(map(int, input().split()))
    # O(10 * n)

    dp = [0] * (n + 1)

    for i in range(n):
        for j in range(9):
            k = i + cost[j]
            if k > n:
                continue
            dp[k] = max(dp[k], dp[i] * 10 + j + 1)
    print(dp[-1])

    ...


main()
