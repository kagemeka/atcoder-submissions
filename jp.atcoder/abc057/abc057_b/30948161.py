def main() -> None:
    n, m = map(int, input().split())
    ab = [tuple(map(int, input().split())) for _ in range(n)]
    cd = [tuple(map(int, input().split())) for _ in range(m)]

    for a, b in ab:
        min_dist = 1 << 30
        index = -1
        for i in range(m):
            c, d = cd[i]
            dist = abs(a - c) + abs(b - d)
            if dist >= min_dist:
                continue
            index = i
            min_dist = dist
        print(index + 1)


if __name__ == "__main__":
    main()
