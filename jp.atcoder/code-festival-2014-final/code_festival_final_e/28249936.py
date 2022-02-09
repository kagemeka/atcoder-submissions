import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))

    cnt = 1

    flg = 0
    for i in range(n - 1):
        if a[i + 1] == a[i]: continue
        if a[i + 1] > a[i] and flg <= 0:
            cnt += 1
            flg = 1
        elif a[i + 1] < a[i] and flg >= 0:
            cnt += 1
            flg = -1
    print(0 if cnt < 3 else cnt)

main()
