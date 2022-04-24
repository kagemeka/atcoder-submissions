import math


def lcm(a: int, b: int) -> int:
    return a // math.gcd(a, b) * b


def solve() -> int:
    n, a, b, x, y, z = map(int, input().split())
    y = min(y, a * x)
    z = min(z, b * x)
    if a > b:
        a, b = b, a
        y, z = z, y

    # if y >= \sqrt{N}, we can brute force a because a * y <= N <= 10^9
    # otherwise if z > \sqrt{N}, we can brute force b.
    # what's about the case both y and z are small?
    # N' := N % lcm(a, b)
    # and initial cost is min((N - N') / a * y, (N - N') / b * z)
    # then, we can brute force a or b.

    l = lcm(a, b)
    m = n // l * l
    if m >= l:
        m -= l
    cost_0 = min(m // a * y, m // b * z)
    n -= m
    # brute force the b count.

    INF = 1 << 62
    mn_cost = INF
    for i in range(n // b + 1):
        j, k = divmod(n - i * b, a)
        mn_cost = min(mn_cost, i * z + j * y + k * x)
    assert mn_cost != INF
    return cost_0 + mn_cost


def main() -> None:
    t = int(input())
    res = []
    for _ in range(t):
        res.append(solve())
    print(*res, sep="\n")


if __name__ == "__main__":
    main()
