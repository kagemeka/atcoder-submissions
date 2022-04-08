def main() -> None:
    # find a loop and the starting point

    # if loop point is positive, get as much as possible

    n, k = map(int, input().split())

    p = list(map(lambda x: int(x) - 1, input().split()))
    c = list(map(int, input().split()))

    inf = 1 << 60
    mx = -inf

    for i in range(n):
        score = [-inf] * n
        score[i] = 0
        order = [-1] * n
        order[i] = 0
        for _ in range(n):
            x = p[i]
            if score[x] != -inf:
                loop_size = order[i] + 1 - order[x]
                loop_score = score[i] + c[x] - score[x]
                break
            order[x] = order[i] + 1
            score[x] = score[i] + c[x]
            i = x
        else:
            raise
        for i in range(n):  # terminal
            if order[i] > k:
                continue
            s = score[i]
            loop_count = (k - order[i]) // loop_size
            if order[i] == 0 and (loop_score <= 0 or loop_size == 0):
                continue
            if loop_score > 0 and order[i] >= order[x]:
                s += loop_count * loop_score
            mx = max(mx, s)
    print(mx)


if __name__ == "__main__":
    main()
