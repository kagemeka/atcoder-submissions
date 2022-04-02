def main() -> None:
    n = int(input())

    def f(a: int, b: int) -> int:
        return a**3 + (a + b) * a * b + b**3

    def binary_search(a: int) -> int:
        lo = -1
        hi = 1 << 20
        while hi - lo > 1:
            # print(lo, hi)
            b = (lo + hi) // 2
            if f(a, b) >= n:
                hi = b
            else:
                lo = b
        return hi

    mn = 1 << 64
    for a in range(1 << 20):
        b = binary_search(a)
        x = f(a, b)
        mn = min(mn, x)
    print(mn)


if __name__ == "__main__":
    main()
