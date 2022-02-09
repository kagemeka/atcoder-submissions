import sys
import numpy as np
from scipy.sparse.csgraph import dijkstra
from scipy.sparse import csr_matrix

I = np.array(sys.stdin.read().split(), dtype=np.int64)
h, w = I[:2]
c = I[2:102].reshape(10, 10).T
a = I[102:].reshape(h, w)

def main():
    cost = dijkstra(csr_matrix(c), directed=True, indices=1).astype(np.int64)

    return np.sum(cost[a[a != -1]])

if __name__ == '__main__':
    ans = main()
    print(ans)
