import sys
import functools

sys.setrecursionlimit(1 << 20)


def main() -> None:
    x = int(input())
    MOD = 998_244_353

    @functools.lru_cache(maxsize=None)
    def dfs(x: int) -> int:
        if x <= 4:
            return x
        return dfs(x // 2) * dfs((x + 1) // 2) % MOD

    print(dfs(x))


if __name__ == "__main__":
    main()
