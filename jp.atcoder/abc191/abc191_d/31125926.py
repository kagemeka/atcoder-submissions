def count_circle_lattice_points(cx: int, cy: int, r: int, k: int) -> int:
    """
    count up integer point (x, y) in the circle
    centered at (cx, cy) with radius r.
    and both x and y are multiple of k.

    """
    assert r >= 0 and k >= 0
    cx %= k
    cy %= k

    def is_ok(dx: int, dy: int) -> bool:
        return dx * dx + dy * dy <= r * r

    def count_right(cx: int, cy: int, x0: int) -> int:
        assert x0 == 0 or x0 == k
        y0, y1 = 0, 1
        count = 0
        for x in range((cx + r) // k * k, x0 - 1, -k):
            while is_ok(x - cx, y0 * k - cy):
                y0 -= 1
            while is_ok(x - cx, y1 * k - cy):
                y1 += 1
            count += y1 - y0 - 1
        return count

    return count_right(cx, cy, k) + count_right(-cx, cy, 0)


def main() -> None:
    K = 10**4

    def normalize(number: str) -> int:
        parts = number.split(".")
        if len(parts) == 1:
            return int(parts[0]) * K
        a, b = parts
        return int(a) * K + int(b) * 10 ** (4 - len(b))

    cx, cy, r = map(normalize, input().split())
    print(count_circle_lattice_points(cx, cy, r, K))


if __name__ == "__main__":
    main()
