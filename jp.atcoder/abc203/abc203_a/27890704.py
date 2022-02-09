import typing


def main() -> typing.NoReturn:
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1]:
        print(a[2])
    elif a[1] == a[2]:
        print(a[0])
    else:
        print(0)

main()
