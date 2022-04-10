def main() -> None:
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    q = list(map(lambda x: int(x) - 1, input().split()))

    # find cycle lengths
    # fibonacci
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

    fib = [0, 1]
    K = 1 << 18
    for _ in range(K):
        fib.append((fib[-1] + fib[-2]) % MOD)

    p = 1
    for c in counts:
        if c == 1:
            continue
        p *= (fib[c + 1] + fib[c - 1]) % MOD
        p %= MOD
    print(p)


if __name__ == "__main__":
    main()
