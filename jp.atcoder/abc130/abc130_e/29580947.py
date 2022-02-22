import sys
import functools

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    MOD = 10 ** 9 + 7

    @functools.lru_cache(maxsize=None)
    def count(i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 1
        cnt = count(i - 1, j) + count(i, j - 1) - count(i - 1, j - 1)
        cnt += count(i - 1, j - 1) * (a[i - 1] == b[j - 1])
        return cnt % MOD

    print(count(n, m))


if __name__ == "__main__":
    main()
