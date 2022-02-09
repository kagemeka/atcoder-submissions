import typing


def main() -> typing.NoReturn:
    s = input()
    i = s.find('C')
    if i == -1:
        print('No')
        return

    i = s[i + 1:].find('F')
    if i == -1:
        print('No')
        return
    print('Yes')

main()
