import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import dijkstra

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
u, v, l = I[2:].reshape(-1, 3).T
u -= 1
v -= 1

def main():
    G = np.zeros((n, n))
    G[u, v] = G[v, u] = l
    adjascent = v[u == 0]
    if adjascent is None:
        return -1
    res = []
    for a in adjascent:
        g = np.copy(G)
        g[0, a] = g[a, 0] = 0
        dist = dijkstra(csgraph=csr_matrix(g), directed=False, indices=a)
        res.append(dist[0] + G[0, a])
    ans = np.amin(res)
    if ans == np.inf:
        return -1
    else:
        return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
