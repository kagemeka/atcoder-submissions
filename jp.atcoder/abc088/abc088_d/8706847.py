import sys
import numpy as np
from heapq import heappop, heappush

# A* algorithm (Dijikstraの発展形) を使う
# Dijikstraでは始点からの距離が短い頂点から探索していくが、A*は終点からの距離が近い頂点から順に探索していくので計算量は少なくなる傾向にある。
# ただしA* algorithm では予め終点までの推定距離が分かっている必要がある。
def main():
    H, W = map(int, sys.stdin.readline().split())

    grid = np.array([list(sys.stdin.readline().rstrip()) for _ in range(H)], dtype='U')
    grid = np.pad(grid, 1, mode='constant')
    # atcoderではnp.pad() のargにconstant_valuesを指定できないみたい


    i = j = 1 # start
    c = 0     # real cost
    h = (H - 1) + (W - 1) # goalまでの推定cost
    s = c + h # score
    q = [] # open list
    heappush(q, (s, c, i, j))
    visited = set() # closed list

    # 今回は最短距離を求めれば良いので必要ないが、最短経路を求める場合には親nodeの記録が必要
    # parent = [[None] * (W + 1) for _ in range(H+1)]

    can_go = False
    while q:
        s, c, i, j = heappop(q)
        visited.add((i, j))
        if c == s:
            can_go = True
            break
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            y = i + dy
            x = j + dx
            if grid[y][x] == '.' and not (y, x) in visited:
                visited.add((y, x))
                # parent[y][x] = (i, j)
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
