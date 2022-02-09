import typing


def main() -> typing.NoReturn:
    n = int(input())

    s = [input() for _ in range(n)]

    cnt = 0
    ca = 0
    cb = 0
    cab = 0
    for w in s:
        cnt += w.count('AB')
        ca += w[-1] == 'A'
        cb += w[0] == 'B'
        cab += w[-1] == 'A' and w[0] == 'B'

    if ca != cb:
        cnt += min(ca, cb)
    else:
        cnt += ca - (cab == ca)

    print(cnt)

main()
