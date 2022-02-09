import typing
import functools
import sys
sys.setrecursionlimit(1 << 20)


def main() -> typing.NoReturn:
    n, k = map(int, input().split())

    MOD = 998_244_353

    @functools.lru_cache(maxsize=None)
    def dfs(n: int, k: int) -> int:
        if k > n: return 0
        if k == 0:
            if n == 0: return 1
            else: return 0
        return (dfs(n - 1, k - 1) + dfs(n, 2 * k)) % MOD

    print(dfs(n, k))

main()
