import typing
import sys

def main() -> typing.NoReturn:
    n = int(input())
    s = [x == 'AND' for x in sys.stdin.read().split()]

    cnts = []
    cnt = 1
    for x in s:
        if x:
            cnt += 1
            continue
        cnts.append(cnt)
        cnt = 1
    cnts.append(cnt)
    p = 1
    for cnt in cnts:
        p *= (1 << cnt) - 1
    print((1 << (n + 1)) - p)

main()
