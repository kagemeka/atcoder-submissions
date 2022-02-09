import sys

b = [[int(x) for x in sys.stdin.readline().split()] for _ in range(2)]
c = [[int(x) for x in sys.stdin.readline().split()] for _ in range(3)]

situation = dict()
def optimize(board, moves):
    if moves == 9:
        tot1 = tot2 = 0
        for i in range(2):
            for j in range(3):
                if board[i][j] == board[i+1][j]:
                    tot1 += b[i][j]
                else:
                    tot2 += b[i][j]
        for i in range(3):
            for j in range(2):
                if board[i][j] == board[i][j+1]:
                    tot1 += c[i][j]
                else:
                    tot2 += c[i][j]
        return tot1, tot2
    results = []
    p = (moves & 1) + 1
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                nxt_board = []
                for k in range(3):
                    row = []
                    for l in range(3):
                        if board[k][l]:
                            row.append(board[k][l])
                        elif k == i and l == j:
                            row.append(p)
                        else:
                            row.append(0)
                    nxt_board.append(tuple(row))
                nxt_board = tuple(nxt_board)
                if nxt_board in situation:
                    results.append(situation[nxt_board])
                else:
                    res = optimize(nxt_board, moves+1)
                    results.append(res)
                    situation[nxt_board] = res
    results.sort()
    return results[0] if p == 2 else results[-1]

def main():
    board = tuple(tuple(0 for _ in range(3)) for _ in range(3))
    res = optimize(board, 0)
    print(*res, sep='\n')

if __name__ ==  '__main__':
    main()
