import typing
import collections
import string

def main() -> typing.NoReturn:
    n = int(input())
    cnt = collections.Counter()
    for c in string.ascii_lowercase:
        cnt[c] = 1 << 20

    for _ in range(n):
        tmp = collections.Counter(input())
        for c in cnt.keys():
            cnt[c] = min(cnt[c], tmp[c])

    t = ''
    for c in string.ascii_lowercase:
        t += c * cnt[c]
    print(t)

main()
