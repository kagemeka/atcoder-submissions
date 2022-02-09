import typing
import functools
import sys
sys.setrecursionlimit(1 << 20)

def main() ->  typing.NoReturn:
    n = int(input())

    # Ex(k) = k / n * (Ex(k) + 1) + (n - k) / n * (Ex(k + 1) + 1)
    # <-> Ex(k) = Ex(k + 1) + n / (n - k)

    @functools.lru_cache(maxsize=None)
    def compute_expectation(current_size: int) -> float:
        if current_size == n: return 0
        return compute_expectation(current_size + 1) + n / (n - current_size)

    print(compute_expectation(1))

main()
