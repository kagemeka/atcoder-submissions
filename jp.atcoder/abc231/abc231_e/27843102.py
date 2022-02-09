import typing
import functools

def main() -> typing.NoReturn:
    n, x = map(int, input().split())
    # dp

    a = list(map(int, input().split()))
    @functools.lru_cache(maxsize=None)
    def f(x: int, i: int) -> int:
        if i == 0:
            return x
        q, r = divmod(x, a[i])
        return min(q + f(r, i - 1), q + 1 + f(a[i] - r, i - 1))
    print(f(x, n - 1))



main()
