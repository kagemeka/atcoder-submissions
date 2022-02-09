import typing


def main() -> typing.NoReturn:
    k = int(input())
    x = 7
    for i in range(k):
        if x % k == 0:
            print(i + 1)
            return
        x = (x * 10 + 7) % k
    print(-1)

main()
