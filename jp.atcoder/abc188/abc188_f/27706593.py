import typing
import functools

def main() -> typing.NoReturn:
    x, y = map(int, input().split())

    @functools.lru_cache(maxsize=None)
    def count(y: int) -> int:
        if y == 1: return x - y
        if y % 2 == 0:
            return min(count(y // 2) + 1, abs(y - x))
        else:
            return min(count(y + 1) + 1, count(y - 1) + 1, abs(y - x))

    print(count(y))


main()
