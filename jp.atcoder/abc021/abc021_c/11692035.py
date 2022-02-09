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
graph = np.logical_or(graph, graph.T)

def main():
    paths = np.zeros(n, dtype=np.int64).reshape(-1, 1)
    paths[a, 0] = 1
    while not paths[b, 0]:
        paths = np.dot(graph, paths)
        paths %= MOD

    print(paths[b, 0])

if __name__ == '__main__':
    main()
