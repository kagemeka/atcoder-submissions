def main() -> None:
    # find a loop and the starting point

    # if loop point is positive, get as much as possible

    n, k = map(int, input().split())

    p = list(map(lambda x: int(x) - 1, input().split()))
    c = list(map(int, input().split()))

    def compute(start: int) -> int:
        order = [-1] * n
        s = []
        i = start
        for j in range(n + 1):
            i = p[i]
            if order[i] != -1:
                loop_start = i
                loop_size = j - order[i]
                break
            order[i] = j
            s.append(c[i])

        loop_score = sum(s[order[loop_start]:])

        mx = -(1 << 60)
        current_score = 0
        rem = k
        i = start
        for _ in range(order[loop_start]):
            rem -= 1
            i = p[i]
            current_score += c[i]
            mx = max(mx, current_score)
            if not rem:
                return mx
        q, rem = divmod(rem, loop_size)
        if q >= 1:
            rem += loop_size
            q -= 1
        if loop_score > 0:
            current_score += q * loop_score
        for _ in range(rem):
            i = p[i]
            current_score += c[i]
            mx = max(mx, current_score)
        return mx

    mx = -(1 << 60)
    for i in range(n):
        mx = max(mx, compute(i))
    print(mx)


if __name__ == "__main__":
    main()
