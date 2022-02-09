import typing
import collections


def main() -> typing.NoReturn:
    n = int(input())
    cnt = collections.Counter()
    for _ in range(n):
        s = input()
        cnt[s] += 1

    res = sorted(cnt.items(), key=lambda x: -x[1])
    print(res[0][0])

main()
