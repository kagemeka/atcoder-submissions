import typing
import sys
sys.setrecursionlimit(1 << 20)
import functools


def main() -> typing.NoReturn:
    a, b, c = map(int, input().split())


    @functools.lru_cache(maxsize=None)
    def dfs(x: int, y: int, z: int) -> float:
        if x == 100 or y == 100 or z == 100:
            return 0
        s = x + y + z
        return (x * dfs(x + 1, y, z) + y * dfs(x, y + 1, z) + z * dfs(x, y, z + 1)) / s + 1
    print(dfs(a, b, c))

main()
