def main() -> None:
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    d = [x[i + 1] - x[i] for i in range(m - 1)]
    d.sort()
    print(sum(d[: max(0, m - n)]))


if __name__ == "__main__":
    main()
