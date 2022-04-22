def popcount(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def main() -> None:
    # inclusion exclusion principle
    n, l = map(int, input().split())
    strings = [input() for _ in range(n)]
    char_set = [0] * n
    for i in range(n):
        # s = strings[i]
        for c in strings[i]:
            char_set[i] |= 1 << ord(c) - 97

    MOD = 998_244_353
    tot = 0
    for s in range(1, 1 << n):
        common_set = (1 << 26) - 1
        for i in range(n):
            if ~s >> i & 1:
                continue
            common_set &= char_set[i]
        tot += (-1) ** (popcount(s) + 1) * pow(popcount(common_set), l, MOD) % MOD
        tot %= MOD
    print(tot)


if __name__ == "__main__":
    main()
