import sys
import numpy as np
from heapq import heappop, heappush

# A* algorithm (Dijikstraの応用)
# Dijikstra: actual cost の順
# A*: score( actual_cost + heuristic cost) の順(scoreが同じ場合はactual_costの順)
# ただしA* algorithm は hueristic_costが計算できるのが前提。また、全頂点への始点からの距離を求めるならDijikstraを使う。今回はstart, endが決まっているのでA*を使った。
def main():
    H, W = map(int, sys.stdin.readline().split())

    grid = np.array([list(sys.stdin.readline().rstrip()) for _ in range(H)], dtype='U')
    grid = np.pad(grid, 1, mode='constant')
    # atcoderではnp.pad() のargにconstant_valuesを指定できないみたい


    i = j = 1             # start
    c = 0                 # real cost
    h = (H - 1) + (W - 1) # heuristic cost
    s = c + h             # score
    q = []                # status: open
    heappush(q, (s, c, i, j))
    visited = set()       # status: closed

    # 今回は最短距離を求めれば良いので必要ないが、最短経路を求める場合にはparent_nodeの記録が必要
    parent = [[None] * (W + 1) for _ in range(H+1)]

    can_go = False
    while q:
        s, c, i, j = heappop(q)
        if (i, j) in visited:
            continue
        visited.add((i, j))
        if c == s: # h == 0 ならそこがgoal
            can_go = True
            break
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            y = i + dy
            x = j + dx
            if grid[y][x] == '.' and not (y, x) in visited:
                parent[y][x] = (i, j)
                h = (H - y) + (W - x)
                s = h + c + 1
                heappush(q, (s, c+1, y, x))

    if can_go:
        ans = np.sum(grid == '.') - (c + 1)
    else:
        ans = -1
    print(ans)


    # 経路も求める場合はこんな感じ
    # i, j = H, W
    # res = [(H, W)]
    # while parent[i][j]:
    #     i, j = parent[i][j]
    #     res.append((i, j))
    # res = list(reversed(res))
    # print(res)

if __name__ == "__main__":
    main()
