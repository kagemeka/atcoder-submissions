import typing


def main() -> typing.NoReturn:
    s = input()
    acgt = set('ACGT')

    mx = 0
    cnt = 0
    for x in s:
        if x in acgt:
            cnt += 1
            continue
        mx = max(mx, cnt)
        cnt = 0
    mx = max(mx, cnt)
    print(mx)

main()
