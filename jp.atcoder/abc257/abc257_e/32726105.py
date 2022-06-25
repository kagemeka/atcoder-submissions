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

    # (10x)^n > (10x + 9)^(n - 1)
    # # knapsack
    # max_cnt = [0] * n

    dp = [0] * (n + 1)  # max_cnt

    for i in range(n):
        for j in range(9):
            k = i + cost[j]
            if k > n:
                continue
            dp[k] = max(dp[k], dp[i] + 1)
            # dp[k] = max(dp[k], dp[i] * 10 + j + 1)

    a = []
    i = n
    while i > 0:
        mx_cnt = -1
        l = -1
        for j in range(9):
            k = i - cost[j]
            if k < 0:
                continue
            if dp[k] >= mx_cnt:
                mx_cnt = dp[k]
                l = j
        if l == -1:
            break
        i -= cost[l]
        a.append(l + 1)

    print("".join(map(str, a)))


main()
