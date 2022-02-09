import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

def main():
    H, W = map(int, sys.stdin.readline().split())
    cost = np.array([sys.stdin.readline().split() for _ in range(10)], dtype=np.int64)
    A = np.array(sys.stdin.read().split(), dtype=np.int64)

    graph = csr_matrix(cost)
    dist = floyd_warshall(csgraph=graph, directed=True)

    ans = dist[np.absolute(A)].T[1].astype(np.int64).sum()
    print(ans)

if __name__ == "__main__":
    main()
