def main() -> None:
    h, w = map(int, input().split())

    a = [list(map(int, input().split())) for _ in range(h)]

    def on_board(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w

    dyx = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    MOD = 10**9 + 7
    sorted_index = sorted(
        [(i, j) for i in range(h) for j in range(w)],
        key=lambda x: a[x[0]][x[1]],
    )

    count = [[1] * w for _ in range(h)]
    for y, x in sorted_index:
        count[y][x] %= MOD
        for dy, dx in dyx:
            ny, nx = y + dy, x + dx
            if not on_board(ny, nx):
                continue
            if a[ny][nx] <= a[y][x]:
                continue
            count[ny][nx] += count[y][x]
    print(sum(sum(count[i]) % MOD for i in range(h)) % MOD)


if __name__ == "__main__":
    main()
