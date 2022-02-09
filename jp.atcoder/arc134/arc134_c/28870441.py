import typing


def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    MOD = 998_244_353
    if a[0] < k:
        print(0)
        return
    a[0] -= k
    s = sum(a[1:])
    if a[0] < s:
        print(0)
        return

    def invert(x: int) -> int:
        return pow(x, MOD - 2, MOD)

    inverse_table = [invert(i) for i in range(k)]
    inverse_table[0] = 1

    def choose(n: int, k: int) -> int:
        assert 0 <= k <= n
        c = 1
        for i in range(k):
            c = c * (n - i) % MOD * inverse_table[i + 1] % MOD
        return c

    res = 1
    for x in a[1:]:
        res *= choose(x + k - 1, k - 1)
        res %= MOD
        a[0] -= x
    res *= choose(a[0] + k - 1, k - 1)
    res %= MOD
    print(res)


if __name__ == "__main__":
    main()
