import typing


def popcount(n: int) -> int:
    r"""Popcount.

    O(1)
    """
    n -= (n >> 1) & 0x5555555555555555
    n = (n & 0x3333333333333333) + ((n >> 2) & 0x3333333333333333)
    n = (n + (n >> 4)) & 0x0f0f0f0f0f0f0f0f
    n = n + (n >> 8)
    n = n + (n >> 16)
    n = n + (n >> 32)
    return n & 0x0000007f


def main() -> typing.NoReturn:
    n, x, y = map(int, input().split())
    # bit DP
    # do all operation 2 before operation 1.

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))


    inf = 1 << 60
    dp = [inf] * (1 << n)
    dp[0] = 0 # nothing

    for s in range(1 << n):
        j = popcount(s) - 1
        for i in range(n):
            if ~s >> i & 1: continue
            t = s & ~(1 << i)
            v = dp[t] + x * abs(b[j] - a[i]) + y * popcount(t >> (i + 1))
            dp[s] = min(dp[s], v)
    print(dp[-1])

main()
