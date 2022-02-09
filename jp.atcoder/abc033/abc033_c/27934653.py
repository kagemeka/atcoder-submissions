import typing


def main() -> typing.NoReturn:
    s = input()
    cnt = 0
    for x in s.split('+'):
        cnt += not '0' in x
    print(cnt)

main()
