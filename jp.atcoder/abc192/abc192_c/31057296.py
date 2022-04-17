def main() -> None:
    n, k = map(int, input().split())

    def g1(n: int) -> int:
        return int("".join(sorted(str(n), reverse=True)))

    def g2(n: int) -> int:
        return int("".join(sorted(str(n))))

    def f(n: int) -> int:
        return g1(n) - g2(n)

    for _ in range(k):
        n = f(n)
    print(n)


if __name__ == "__main__":
    main()
