def main() -> None:
    n = int(input())
    s = [list(map(lambda x: int(x) - 1, input())) for _ in range(n)]

    time = [[-1] * 10 for _ in range(n)]
    for i in range(n):
        for j in range(10):
            time[i][s[i][j]] = j

    mn = 1 << 60
    for d in range(10):
        count = [0] * 10
        mx = 0
        for i in range(n):
            t = time[i][d]
            count[t] += 1
            t += 10 * (count[t] - 1)
            mx = max(mx, t)
        mn = min(mn, mx)
    print(mn)


if __name__ == "__main__":
    main()
