import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall, csgraph_to_dense
from scipy.sparse import csr_matrix
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
u, v, l = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(-1, 3).T
u -= 1; v -= 1
graph = csgraph_to_dense(csr_matrix((l, (u, v)), shape=(n, n)))
graph += np.transpose(graph)
graph[graph == 0] = np.inf
dist0 = graph[0].copy()
graph[0] = 0; graph[:, 0] = 0

def main():
    dist = floyd_warshall(graph, directed=False)
    x, y = np.array(list(combinations(range(1, n), 2))).T
    res = np.amin(dist0[x] + dist0[y] + dist[y, x])
    print(-1 if res == np.inf else int(res))

if __name__ ==  '__main__':
    main()
