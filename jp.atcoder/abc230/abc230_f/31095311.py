from __future__ import annotations
import collections
import typing

T = typing.TypeVar("T")


def number_of_subsequences(arr: list[T], mod: int | None = None) -> int:
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    prev_index: typing.DefaultDict[T, int] = collections.defaultdict(int)
    for i in range(n):
        j, prev_index[arr[i]] = prev_index[arr[i]], i + 1
        dp[i + 1] = dp[i] * 2
        if j != 0:
            dp[i + 1] -= dp[j - 1]
        if mod:
            dp[i + 1] %= mod
    return dp[-1]


def main() -> None:
    MOD = 998_244_353

    n = int(input())
    a = list(map(int, input().split()))
    s = a.copy()
    for i in range(n - 1):
        s[i + 1] += s[i]
    print(number_of_subsequences(s[:-1], MOD))


if __name__ == "__main__":
    main()
