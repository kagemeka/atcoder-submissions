def main() -> None:
    N = 10
    p = int(input())
    fact = list(range(N + 1))
    fact[0] = 1
    for i in range(N):
        fact[i + 1] *= fact[i]

    count = 0
    for i in range(N, 0, -1):
        cnt = min(100, p // fact[i])
        count += cnt
        p -= cnt * fact[i]
        if p:
            continue
        print(count)
        return


main()
