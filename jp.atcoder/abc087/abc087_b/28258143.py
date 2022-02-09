import typing


def main() -> typing.NoReturn:
    a = int(input())
    b = int(input())
    c = int(input())

    x = int(input())
    cnt = 0
    for i in range(a + 1):
        for j in range(b + 1):

            k = (x - 500 * i - 100 * j) // 50
            cnt += 0 <= k <= c
    print(cnt)

main()
