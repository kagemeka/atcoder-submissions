import typing


def main() -> typing.NoReturn:
    s = input()

    prev = ''
    t = ''
    cnt = 0
    for c in s:
        t += c
        if t == prev: continue
        cnt += 1
        prev = t
        t = ''
    print(cnt)

main()
