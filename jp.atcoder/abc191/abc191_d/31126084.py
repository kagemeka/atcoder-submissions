def count_circle_lattice_points_binary_search(
    cx: int,
    cy: int,
    r: int,
    k: int,
) -> int:
    """
    count up integer point (x, y) in the circle
    centered at (cx, cy) with radius r.
    and both x and y are multiple of k.

    """
    assert r >= 0 and k >= 0

    def count_up_y(x: int) -> int:
        assert x % k == 0
        rhs = r * r - (x - cx) ** 2

        if rhs < 0:
            return 0

        def is_ok(y: int) -> bool:
            return (y - cy) ** 2 <= rhs

        def search_max() -> int:
            lo, hi = cy, cy + r + 1
            while hi - lo > 1:
                y = (lo + hi) >> 1
                if is_ok(y):
                    lo = y
                else:
                    hi = y
            return lo // k * k

        def search_min() -> int:
            lo, hi = cy - r - 1, cy
            while hi - lo > 1:
                y = (lo + hi) >> 1
                if is_ok(y):
                    hi = y
                else:
                    lo = y
            return (hi + k - 1) // k * k

        return (search_max() - search_min()) // k + 1

    x0 = (cx - r + k - 1) // k * k
    x1 = (cx + r) // k * k
    return sum(count_up_y(x) for x in range(x0, x1 + 1, k))


def main() -> None:
    K = 10**4

    def normalize(number: str) -> int:
        parts = number.split(".")
        if len(parts) == 1:
            return int(parts[0]) * K
        a, b = parts
        return int(a) * K + int(b) * 10 ** (4 - len(b))

    cx, cy, r = map(normalize, input().split())
    print(count_circle_lattice_points_binary_search(cx, cy, r, K))


if __name__ == "__main__":
    main()
