import typing
import collections


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    cnt = collections.defaultdict(int)
    tot = 0
    for i in range(n + 1):
        tot += cnt[s[i] - k]
        cnt[s[i]] += 1
    print(tot)


main()
