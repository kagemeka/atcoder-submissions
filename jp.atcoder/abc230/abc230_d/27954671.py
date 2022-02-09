import typing


def main() -> typing.NoReturn:
    n, d = map(int, input().split())
    lr = [tuple(map(int, input().split())) for _ in range(n)]
    lr.sort(key=lambda x: (x[0], x[1]))
    cnt = 0
    x = 0
    for l, r in lr:
        if l < x: continue
        x = r + d
        cnt += 1
    print(cnt)

main()
