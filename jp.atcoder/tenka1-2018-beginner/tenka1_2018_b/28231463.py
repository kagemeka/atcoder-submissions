import typing


def main() -> typing.NoReturn:
    a, b, k = map(int, input().split())
    cnt = [a, b]
    for i in range(k):
        i &= 1
        c = cnt[i] // 2
        cnt[i] = c
        cnt[i ^ 1] += c
    print(*cnt)

main()
