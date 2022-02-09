import sys
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

n, u, v = map(int, sys.stdin.readline().split())
a, b = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(-1, 2).T - 1
graph = csr_matrix(([1] * (n-1), (a, b)), (n, n))

def main():
    dist_u, dist_v = dijkstra(graph, directed=False, indices=[u-1, v-1])

    ans = np.amax(dist_v[dist_v >= dist_u]) - 1
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
