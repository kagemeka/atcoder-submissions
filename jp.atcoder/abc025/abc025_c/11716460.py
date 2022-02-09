import sys

b = [[int(x) for x in sys.stdin.readline().split()] for _ in range(2)]
c = [[int(x) for x in sys.stdin.readline().split()] for _ in range(3)]

situation = dict()
def optimize(board, moves):
    if moves == 9:
        if board in situation: return situation[board]
        tot1 = tot2 = 0
        for i in range(3):
            for j in range(3):
                if i < 2:
                    if board[i][j] == board[i+1][j]: tot1 += b[i][j]
                    else: tot2 += b[i][j]
                if j < 2:
                    if board[i][j] == board[i][j+1]: tot1 += c[i][j]
                    else: tot2 += c[i][j]
        situation[board] = (tot1, tot2)
        return tot1, tot2
    results = []
    p = (moves & 1) + 1
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                nxt_board =[list(row) for row in board]
                nxt_board[i][j] = p
                nxt_board = tuple(tuple(row) for row in nxt_board)
                if nxt_board in situation:
                    results.append(situation[nxt_board])
                else:
                    res = optimize(nxt_board, moves+1)
                    results.append(res)
                    situation[nxt_board] = res
    results.sort()
    return results[0] if p == 2 else results[-1]

def main():
    board = tuple((0, 0, 0) for _ in range(3))
    res = optimize(board, 0)
    print(*res, sep='\n')

if __name__ ==  '__main__':
    main()
