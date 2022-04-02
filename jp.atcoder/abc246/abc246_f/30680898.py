def main() -> None:
    n, l = map(int, input().split())

    MOD = 998_244_353
    s = [input() for _ in range(n)]
    char_set = [0] * n
    for i in range(n):
        for char in s[i]:
            char_set[i] |= 1 << ord(char) - ord("a")

    tot = 0
    for i in range(n):
        for u in range(1 << i):
            common_set = char_set[i]
            row_count = 1
            for j in range(n):
                if ~u >> j & 1:
                    continue
                common_set &= char_set[j]
                row_count += 1
            common_count = bin(common_set).count("1")
            cnt = pow(common_count, l, MOD)
            tot += cnt * (-1 + (row_count & 1) * 2)
            tot %= MOD
    print(tot)


if __name__ == "__main__":
    main()
