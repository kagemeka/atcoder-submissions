def main() -> None:
    N = 19
    board = [input() for _ in range(N)]

    def is_winner(mark: str, k: int) -> bool:
        for i in range(N - k + 1):
            for j in range(N):
                if all(board[i + d][j] == mark for d in range(k)):
                    return True
        for i in range(N):
            for j in range(N - k + 1):
                if all(board[i][j + d] == mark for d in range(k)):
                    return True
        for i in range(N - k + 1):
            for j in range(N - k + 1):
                if all(board[i + d][j + d] == mark for d in range(k)):
                    return True
        for i in range(k - 1, N):
            for j in range(N - k + 1):
                if all(board[i - d][j + d] == mark for d in range(k)):
                    return True
        return False

    def count_up(mark: str) -> int:
        return sum(row.count(mark) for row in board)

    black_count = count_up("o")
    white_count = count_up("x")
    black_win = is_winner("o", 5)
    white_win = is_winner("x", 5)

    if black_win and white_win:
        res = False
    elif black_win:
        res = not is_winner('o', 10) and black_count == white_count + 1
    elif white_win:
        res = not is_winner('x', 10) and black_count == white_count
    else:
        res = 0 <= black_count - white_count <= 1
    print("YES" if res else "NO")


if __name__ == "__main__":
    main()
