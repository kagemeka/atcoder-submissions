import typing
import sys



def main() -> typing.NoReturn:
    n, d = map(int, input().split())
    lr = [list(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: (x[1], x[0]))

    cnt = 0
    x = 0
    for l, r in lr:
        if l < x: continue
        cnt += 1
        x = r + d
    print(cnt)

main()
