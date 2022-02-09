import sys
import numpy as np
from scipy.sparse.csgraph import dijkstra, csgraph_to_dense
from scipy.sparse import csr_matrix

MOD = 10 ** 9 + 7
n, a, b, m, *uv = map(int, sys.stdin.read().split())
a -= 1; b -= 1
u, v = np.array(uv, dtype=np.int8).reshape(-1, 2).T - 1
csgraph = csr_matrix((np.ones(m), (u, v)), shape=(n, n))
graph = csgraph_to_dense(csgraph=csgraph)
graph += graph.T

def main():
    dist = dijkstra(csgraph=csgraph, indices=a, directed=False).astype(np.int8)
    paths = np.zeros(n, dtype=np.int64)
    paths[a] = 1
    for d in range(dist[b]):
        u = np.where(dist == d)[0]
        v = np.where(dist == d + 1)[0]
        paths[v] = np.sum(paths[u] * graph[:, u][v], axis=1)
        paths[v] %= MOD

    print(paths[b])

if __name__ == '__main__':
    main()
