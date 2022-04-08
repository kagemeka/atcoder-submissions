import functools
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n, k = map(int, input().split())
    q, k = divmod(k, n)
    MOD = 10**9 + 7

    @functools.lru_cache(maxsize=None)
    def choose(n: int, k: int) -> int:
        if not 0 <= k <= n:
            return 0
        if k == 0:
            return 1
        return (choose(n - 1, k) + choose(n - 1, k - 1)) % MOD

    if q > 0:
        print(choose(n, k))
    else:
        print(choose(n + k - 1, k))


if __name__ == "__main__":
    main()
