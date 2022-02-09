import typing



def main() -> typing.NoReturn:
    h, w = map(int, input().split())
    board = [
        [0 if x == '.' else int(x) for x in input()]
        for _ in range(h)
    ]
    dyx = ((-1, 0), (0, -1), (1, 0), (0, 1))
    def on_board(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w

    for i in range(h):
        for j in range(w):
            if board[i][j] != 0: continue
            s = 1
            for dy, dx in dyx:
                y = i + dy
                x = j + dx
                if not on_board(y, x): continue
                s |= 1 << board[y][x]
            for k in range(1, 6):
                if ~s >> k & 1: break
            board[i][j] = k
    for row in board:
        print(''.join(map(str, row)))

main()
