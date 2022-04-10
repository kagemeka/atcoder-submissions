import sys

sys.setrecursionlimit(1 << 20)
import typing


def main() -> None:
    n = int(input())

    def dfs(n: int) -> typing.List[int]:
        if n == 1:
            return [1]
        a = dfs(n - 1)
        return a + [n] + a

    print(*dfs(n))


if __name__ == "__main__":
    main()
