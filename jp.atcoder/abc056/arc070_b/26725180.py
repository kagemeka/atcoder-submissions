import typing
import sys
import numpy as np



def solve(a: np.ndarray, k: int) -> typing.NoReturn:
    n = len(a)
    a.sort()

    def compute_dp(a: np.ndarray) -> np.ndarray:
        dp = np.zeros((n + 1, k), np.bool8)
        dp[0, 0] = True
        for i in range(n):
            dp[i + 1] |= dp[i]
            dp[i + 1, a[i]:] |= dp[i, :-a[i]]
        return dp
    dp_l = compute_dp(a)
    dp_r = compute_dp(a[::-1])[::-1]
    dp_r = dp_r.astype(np.int64).cumsum(axis=1)

    def is_needed(i: int) -> bool:
        r = dp_r[i + 1]
        x = a[i]
        for j in np.flatnonzero(dp_l[i]).tolist():
            j = k - j - 1
            if not r[j] - (0 if j - x < 0 else r[j - x]) >= 1: continue
            return True
        return False

    def binary_search() -> int:
        lo, hi = -1, n
        while hi - lo > 1:
            i = (lo + hi) >> 1
            if is_needed(i):
                hi = i
            else:
                lo = i
        return hi

    print(binary_search())


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = np.array(sys.stdin.readline().split(), dtype=np.int64)
    solve(a, k)


main()
