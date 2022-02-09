import typing
import functools


def main() -> typing.NoReturn:
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    @functools.lru_cache(maxsize=None)
    def dfs(i: int, x: int) -> typing.Tuple[int, int]:
        if i == 0:
            return x
        q, r = divmod(x, a[i])
        return min(q + dfs(i - 1, r), q + 1 + dfs(i - 1, a[i] - r))

    print(dfs(n - 1, x))

main()
