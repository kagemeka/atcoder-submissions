import typing


def main() -> None:
    n = input()
    digits = list(map(int, n))
    m = int(input())

    # inclusion exclusion principle
    # dp
    # O(10^4 * 2^m)

    a = list(map(int, input().split()))

    MOD = 998_244_353

    def count(ng_digits: typing.List[int]) -> int:
        k = len(ng_digits)
        tot = 45 - sum(ng_digits)
        assert tot >= 0
        dp1 = [0, 0]
        dp1[0] = 1
        dp2 = [0, 0]
        flg = True
        for d in digits:
            m = d
            s = (d) * (d - 1) // 2
            for y in ng_digits:
                if y < d:
                    m -= 1
                    s -= y
            # print(m, s, -1)
            dp2[1] = (dp2[1] * 10 * (10 - k) + tot * dp1[1] + dp2[0] * 10 * m + s * dp1[0]) % MOD
            dp2[0] = (dp2[0] * 10 + d) % MOD if flg else 0
            dp1[1] = (dp1[1] * (10 - k) + dp1[0] * m) % MOD
            dp1[1] += 0 in ng_digits
            if d in ng_digits:
                flg = False
                dp1[0] = dp2[0] = 0
            # print(dp1, dp2, ng_digits)
        # print(sum(dp2) % MOD)
        return sum(dp2) % MOD

    total = 0
    for s in range(1 << m):
        ng_digits = []
        for i in range(m):
            if ~s >> i & 1:
                continue
            ng_digits.append(a[i])
        k = len(ng_digits)
        total += count(ng_digits) * pow(-1, k)
        total %= MOD
    print(total)


main()
