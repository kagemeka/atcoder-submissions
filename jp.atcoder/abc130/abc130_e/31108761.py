import typing

T = typing.TypeVar("T")


def count_common_subsequences(
    a: typing.Sequence[T],
    b: typing.Sequence[T],
    mod: typing.Optional[int],
) -> int:
    n, m = len(a), len(b)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        dp[i + 1][0] = 1
    for j in range(m):
        dp[0][j + 1] = 1
    for i in range(n):
        for j in range(m):
            dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1]
            if a[i] != b[j]:
                dp[i + 1][j + 1] -= dp[i][j]
            if mod:
                dp[i + 1][j + 1] %= mod
    return dp[-1][-1]


def main() -> None:
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    t = list(map(int, input().split()))
    MOD = 10**9 + 7
    print(count_common_subsequences(s, t, MOD))


if __name__ == "__main__":
    main()
