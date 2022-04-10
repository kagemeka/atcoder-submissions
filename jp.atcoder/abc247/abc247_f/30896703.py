def main() -> None:
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    q = list(map(lambda x: int(x) - 1, input().split()))

    # find cycle lengths
    # for each cycle
    # if cycle size is 1, it's needed to be chosen anytime.
    # consider the cases cycle size >= 2
    # suppose cycling pairs are sorted in order of functional graph.
    # if pairs_i is chosen,
    # pairs_{(i + 1) % cycle_size} would satisfy the given constraints
    # regardless it's also chosen or not.
    # if paris_i is not chosen,
    # pairs_{(i + 1) % cycle_size} should be chosen.
    # tips: this dp transitions are gonna be like Fibonacci sequence.

    # be careful of the last.
    # in only the case in which first one has been chosen,
    # we can decide to choose the last one or not. (1st case)
    # in the case in which first one has not been chosen,
    # we should choose the last one. (2nd case)

    # in first case, dp transition becomes like
    # dp_first_chosen = [[0, 1], [1, 1], [1, 2], [2, 3], ...]
    # in second case, it becomes like
    # dp_first_not_chosen = [[1, 0], [0, 1], [1, 1], [1, 2], ...]
    # these dp sequence are just sliding.
    # thus, we can omit one of them in implementation.

    MOD = 998_244_353

    pairs = list(zip(p, q))
    pairs.sort()

    checked = [False] * n
    counts = []
    for i in range(n):
        if checked[i]:
            continue
        checked[i] = True
        count = 1
        while not checked[pairs[i][1]]:
            i = pairs[i][1]
            checked[i] = True
            count += 1
        counts.append(count)

    dp = [[0, 1]]
    for _ in range(n):
        dp.append([dp[-1][1], sum(dp[-1]) % MOD])

    p = 1
    for c in counts:
        if c == 1:
            continue
        p *= (sum(dp[c - 1]) + dp[c - 2][1]) % MOD
        p %= MOD
    print(p)


if __name__ == "__main__":
    main()
