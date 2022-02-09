import typing


def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    cnt = [0] * m
    for _ in range(n):
        k, *a, = map(int, input().split())
        for x in a:
            cnt[x - 1] += 1

    print(cnt.count(n))

main()
