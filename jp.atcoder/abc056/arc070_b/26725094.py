import typing
import sys
import numpy as np



def solve(a: np.ndarray, k: int) -> typing.NoReturn:
    n = len(a)

    def compute_dp(a: np.ndarray) -> np.ndarray:
        dp = np.zeros((n + 1, k), np.bool8)
        dp[0, 0] = True
        for i in range(n):
            dp[i + 1] = dp[i].copy()
            dp[i + 1, a[i]:] |= dp[i, :-a[i]]
        return dp
    dp_l = compute_dp(a)
    dp_r = compute_dp(a[::-1])[::-1]
    dp_r = dp_r.astype(np.int64).cumsum(axis=1)

    cnt = 0
    for p in range(n):
        l, r = dp_l[p], dp_r[n - p]
        x = a[p]
        for i in np.flatnonzero(l).tolist():
            if not r[k - i - 1] - (0 if k - x - i - 1 < 0 else r[k - x - i - 1]) >= 1:
                continue
            cnt += 1
            break
    print(n - cnt)


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    solve(a, k)


main()
