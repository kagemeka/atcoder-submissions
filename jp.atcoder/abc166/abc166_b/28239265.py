import typing


def main() -> typing.NoReturn:
    n, k = map(int, input().split())

    cnt = [0] * n
    for _ in range(k):
        d = int(input())
        a = list(map(int, input().split()))
        for i in a:
            i -= 1
            cnt[i] += 1
    print(sum([c == 0 for c in cnt]))

main()
