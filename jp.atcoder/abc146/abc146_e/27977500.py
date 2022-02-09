import typing
import collections


def main() -> typing.NoReturn:
    # (s_j - s_i) % k = j - i
    # <-> (s_j - j) % k = (s_i - i) % k and j - i < k, (s_i - i) % k = 0 and k > 1
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k == 1:
        print(0)
        return
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
    for i in range(1, n + 1):
        s[i] = (s[i] - i) % k
    cnt = collections.defaultdict(int)
    cnt[0] = 1
    res = 0
    for i in range(1, n + 1):
        res += cnt[s[i]]
        cnt[s[i]] += 1
        if i - (k - 1) >= 0:
            cnt[s[i - (k - 1)]] -= 1
        print(i, res)
    print(res)

main()
