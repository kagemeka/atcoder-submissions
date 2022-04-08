def main() -> None:
    n = int(input())
    k = list(map(int, input().split()))
    inf = 1 << 60
    k = [inf] + k + [inf]
    l = [min(k[i], k[i + 1]) for i in range(n)]
    print(*l)


if __name__ == "__main__":
    main()
