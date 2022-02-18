import typing
import sys

# import itertools
import functools

sys.setrecursionlimit(1 << 20)


def main() -> None:
    x = int(input())
    MOD = 998_244_353

    @functools.lru_cache(maxsize=None)
    def compute(x: int) -> int:
        if x <= 4:
            return x
        x, y = x // 2, (x + 1) // 2
        return compute(x) * compute(y) % MOD

    print(compute(x))


if __name__ == "__main__":
    main()
