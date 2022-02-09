import typing
import collections

def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = s[i] + a[i]
        s[i + 1] %= m


    cnt = collections.Counter()
    tot = 0
    for x in s:
        tot += cnt[x]
        cnt[x] += 1
    print(tot)

main()
