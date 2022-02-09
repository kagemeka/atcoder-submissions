import typing


def main() -> typing.NoReturn:
    h, w, k = map(int, input().split())

    board = [input() for _ in range(h)]

    def satisfy(s: int, t: int) -> bool:
        cnt = 0
        for i in range(h):
            if s >> i & 1: continue
            for j in range(w):
                if t >> j & 1: continue
                cnt += board[i][j] == '#'
        return cnt == k

    cnt = 0
    for s in range(1 << h):
        for t in range(1 << w):
            cnt += satisfy(s, t)
    print(cnt)


main()
