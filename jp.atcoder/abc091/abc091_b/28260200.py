import typing
import collections

def main() -> typing.NoReturn:
    n = int(input())

    cnt = collections.Counter()
    for _ in range(n):
        s = input()
        cnt[s] += 1

    m = int(input())
    for _ in range(m):
        s = input()
        cnt[s] -= 1

    print(max(0, *cnt.values()))

main()
