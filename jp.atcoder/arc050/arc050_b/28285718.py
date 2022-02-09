import typing


def main() -> typing.NoReturn:
    # binary search maximum
    r, b = map(int, input().split())
    x, y = map(int, input().split())

    def possible(k: int) -> bool:
        return (r - k) // (x - 1) + (b - k) // (y - 1) >= k

    def binary_search() -> int:
        lo, hi = 0, 1 << 62

        while hi - lo > 1:
            k = (lo + hi) // 2
            if possible(k):
                lo = k
            else:
                hi = k
        return lo

    print(binary_search())



main()
