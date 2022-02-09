import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(int, input().split()))
    a = [x - 1 for x in a]

    i = 0
    cnt = 0
    for x in a:
        if x == i:
            cnt += 1
            i += 1
    print(n - cnt if cnt else -1)

main()
