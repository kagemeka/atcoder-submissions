def main() -> None:
    n = int(input())
    res = []

    def f(x: int) -> int:
        s = 0
        while x:
            s += x % 10
            x //= 10
        return s

    for x in range(n - 1, max(n - 9 * 18, 0), -1):
        if x + f(x) == n:
            res.append(x)
    print(len(res))
    if len(res):
        print(*res[::-1], sep="\n")


if __name__ == "__main__":
    main()
