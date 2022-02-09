import typing
import collections

def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    s = [0] * (n + 1)
    for i in range(n):
        s[i + 1] = (s[i] + a[i]) % m

    cnt = collections.defaultdict(int)
    tot = 0
    for i in range(n + 1):
        tot += cnt[s[i]]
        cnt[s[i]] += 1
    print(tot)

main()
