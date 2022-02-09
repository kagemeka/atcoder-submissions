import sys
import numpy as np
from scipy.sparse.csgraph import dijkstra, csgraph_to_dense
from scipy.sparse import csr_matrix

MOD = 10 ** 9 + 7
n, a, b, m, *uv = map(int, sys.stdin.read().split())
a -= 1; b -= 1
u, v = np.array(uv).reshape(-1, 2).T - 1
graph = csgraph_to_dense(csr_matrix((np.ones(m), (u, v)), shape=(n, n))).astype(np.int64)
graph += graph.T

def main():
    dist = dijkstra(csgraph=graph, indices=a).astype(np.int64)
    paths = np.zeros(n, dtype=np.int64); paths[a] = 1
    for d in range(dist[b]):
        u = np.where(dist == d)[0]
        v = np.where(dist == d + 1)[0]
        paths[v] = np.sum(paths[u] * graph[:, u][v], axis=1)
        paths[v] %= MOD

    print(paths[b])

if __name__ == '__main__':
    main()
