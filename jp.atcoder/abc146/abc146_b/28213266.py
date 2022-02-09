import typing


def main() -> typing.NoReturn:
    n = int(input())
    s = list(input())
    for i in range(len(s)):
        s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
    print(''.join(s))

main()
