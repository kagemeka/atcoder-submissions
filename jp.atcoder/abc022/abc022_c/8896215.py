import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
u, v, l = I[2:].reshape(-1, 3).T
u -= 1
v -= 1

def main():
    G = np.full((n, n), np.inf)
    G[u, v] = G[v, u] = l

    g = np.copy(G)
    g[0] = g[:, 0] = np.inf
    dist = floyd_warshall(csgraph=csr_matrix(g), directed=False)
    np.fill_diagonal(dist, np.inf)
    dist += G[0] + G[0].reshape(-1, 1)

    ans = np.amin(dist)
    if ans == np.inf:
        return -1
    else:
        return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
