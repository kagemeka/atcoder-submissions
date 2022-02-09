import typing


def main() -> typing.NoReturn:
    s = input()
    n = len(s)
    cnt = 0
    for i in range(n // 2):
        cnt += s[i] != s[n - 1 - i]
    print(cnt)

main()
