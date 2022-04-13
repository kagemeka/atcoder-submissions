def main() -> None:
    n, g = map(int, input().split())
    pc = [tuple(map(int, input().split())) for _ in range(n)]

    # brute-force problem difficulties set
    # such that all of the problems in each difficulty should be solved.

    g //= 100
    mn = 1 << 10
    for s in range(1 << n):
        score = 0
        count = 0
        for i in range(n):
            if ~s >> i & 1:
                continue
            p, c = pc[i]
            score += p * (i + 1) + c // 100
            count += p

        for i in range(n):
            if s >> i & 1:
                continue
            p, _ = pc[i]
            shortage = max(0, (g - score + i) // (i + 1))
            if shortage < p:
                mn = min(mn, count + shortage)
    print(mn)


if __name__ == "__main__":
    main()
