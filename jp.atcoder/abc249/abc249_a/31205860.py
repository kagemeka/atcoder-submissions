def main() -> None:
    a, b, c, d, e, f, x = map(int, input().split())

    def dist(a: int, b: int, c: int, x: int) -> int:

        d = 0
        while x > 0:
            if x <= a:
                d += x * b
                break
            d += a * b
            x -= a + c
        return d

    d0 = dist(a, b, c, x)
    d1 = dist(d, e, f, x)
    print(d0, d1)
    print("Takahashi" if d0 > d1 else "Draw" if d0 == d1 else "Aoki")


if __name__ == "__main__":
    main()
