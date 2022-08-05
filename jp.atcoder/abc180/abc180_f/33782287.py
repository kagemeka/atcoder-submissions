import typing


def cumprod(mod: int, a: typing.List[int]) -> typing.List[int]:
    for i in range(len(a) - 1):
        a[i + 1] *= a[i]
        a[i + 1] %= mod
    return a


def make_factrials(
    p: int,
    size: int,
) -> typing.Tuple[typing.List[int], typing.List[int]]:
    fact = list(range(size))
    fact[0] = 1
    fact = cumprod(p, fact)
    ifact = list(range(size, 0, -1))
    ifact[0] = pow(fact[-1], p - 2, p)
    ifact = cumprod(p, ifact)[::-1]
    return fact, ifact


class FactorialTablesFrequentOps:
    mod: int
    fact: typing.List[int]
    ifact: typing.List[int]

    def __init__(self, p: int, size: int) -> None:
        self.mod = p
        self.fact, self.ifact = make_factrials(p, size)

    def p(self, n: int, k: int) -> int:
        if k < 0 or n < k:
            return 0
        return self.fact[n] * self.ifact[n - k] % self.mod

    def c(self, n: int, k: int) -> int:
        return self.p(n, k) * self.ifact[k] % self.mod

    def h(self, n: int, k: int) -> int:
        return self.c(n - 1 + k, k)

    def inv(self, n: int) -> int:
        return self.fact[n - 1] * self.ifact[n] % self.mod

    def inv_p(self, n: int, k: int) -> int:
        assert 0 <= k <= n
        return self.ifact[n] * self.fact[n - k] % self.mod

    def inv_c(self, n: int, k: int) -> int:
        return self.inv_p(n, k) * self.fact[k] % self.mod


def main() -> None:
    mod = 1_000_000_007
    size = 1 << 10
    f = FactorialTablesFrequentOps(mod, size)
    n, m, l = map(int, input().split())
    path = [1] * size
    path[0] = 0
    for i in range(3, size):
        path[i] = path[i - 1] * i % mod
    cycle = [0] + path

    def g(l: int) -> int:
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(n):
            for k in range(1, l + 1):
                if i + k > n:
                    break
                for j in range(m + 1):
                    x = dp[i][j] * f.c(n - i - 1, k - 1) % mod
                    if j + k <= m:
                        dp[i + k][j + k] += x * cycle[k] % mod
                        dp[i + k][j + k] %= mod
                    if j + k - 1 <= m:
                        dp[i + k][j + k - 1] += x * path[k] % mod
                        dp[i + k][j + k - 1] %= mod
        return dp[-1][-1]

    print((g(l) - g(l - 1)) % mod)


if __name__ == "__main__":
    main()
