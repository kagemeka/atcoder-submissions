import typing


def main() -> typing.NoReturn:
    s = list(input())
    t = list(input())
    n = len(t)
    mn = 1 << 60
    for i in range(len(s) - n + 1):
        mn = min(mn, sum(s[i + j] != t[j] for j in range(n)))
    print(mn)



main()
