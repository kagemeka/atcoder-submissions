import typing


def main() -> typing.NoReturn:
    n, l = map(int, input().split())
    a = [1 if x == '+' else -1 for x in input()]
    cnt = 0
    s = 1
    for d in a:
        s += d
        if s <= l: continue
        cnt += 1
        s = 1
    print(cnt)

main()
