def main() -> None:
    K = 10**4

    def normalize(number: str) -> int:
        parts = number.split(".")
        if len(parts) == 1:
            return int(parts[0]) * K
        a, b = parts
        return int(a) * K + int(b) * 10 ** (4 - len(b))

    cx, cy, r = map(normalize, input().split())

    def count_up_y(x: int) -> int:
        assert x % K == 0
        rhs = r * r - (x - cx) ** 2

        if rhs < 0:
            return 0

        def search_max() -> int:
            lo, hi = cy, cy + r + 1
            while hi - lo > 1:
                y = (lo + hi) >> 1
                lhs = (y - cy) ** 2
                if lhs <= rhs:
                    lo = y
                else:
                    hi = y
            return lo // K * K

        def search_min() -> int:
            lo, hi = cy - r - 1, cy
            while hi - lo > 1:
                y = (lo + hi) >> 1
                lhs = (y - cy) ** 2
                if lhs <= rhs:
                    hi = y
                else:
                    lo = y
            return (hi + K - 1) // K * K

        y_max = search_max()
        y_min = search_min()
        return (y_max - y_min) // K + 1

    x0 = (cx - r + K - 1) // K * K
    x1 = (cx + r) // K * K
    print(sum(count_up_y(x) for x in range(x0, x1 + 1, K)))


if __name__ == "__main__":
    main()
