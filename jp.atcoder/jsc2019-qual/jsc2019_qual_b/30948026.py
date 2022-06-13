def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    K = 1 << 11
    count = [0] * K
    count_0 = 0
    count_1 = 0
    for x in a:
        count_0 += sum(count[x + 1 :])
        count[x] += 1

    for x in a:
        count_1 += sum(count[x + 1 :])

    MOD = 10 ** 9 + 7
    print((count_0 * k % MOD + k * (k - 1) // 2 % MOD * count_1) % MOD)


if __name__ == "__main__":
    main()
