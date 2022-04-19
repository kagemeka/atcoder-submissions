def main() -> None:

    N = 4

    a = [list(map(int, input().split())) for _ in range(4)]

    is_inner = [[False] * N for _ in range(N)]

    state = [[0] * (N + 1) for _ in range(N + 1)]

    def is_ok() -> bool:
        return all(not a[i][j] or is_inner[i][j] for i in range(N) for j in range(N))

    dij = ((-1, 0), (0, -1), (1, 0), (0, 1))

    si, sj = -1, -1

    def dfs(i: int, j: int) -> int:
        assert state[i][j] == 0
        state[i][j] = 1
        count = 0
        for di, dj in dij:
            ni, nj = i + di, j + dj
            if not (0 <= ni <= N and 0 <= nj <= N):
                continue

            def flip() -> None:
                if ni != i:
                    return
                x = min(nj, j)
                for y in range(i, N):
                    is_inner[y][x] ^= True

            flip()

            if state[ni][nj] == 1:
                if ni == si and nj == sj:
                    count += is_ok()
            else:
                count += dfs(ni, nj)
            flip()

        state[i][j] = 0
        return count

    tot = 0
    for i in range(N + 1):
        for j in range(N + 1):
            si, sj = i, j
            tot += dfs(si, sj)
            state[i][j] = 1

    assert tot & 1 == 0
    print(tot // 2)


if __name__ == "__main__":
    main()
