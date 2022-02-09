import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

def main():
    H, W = map(int, sys.stdin.readline().split())
    ca = np.array(sys.stdin.read().split(), dtype=np.int64)
    cost = ca[:100].reshape(10, 10)
    A = ca[100:]

    min_cost = floyd_warshall(csgraph=csr_matrix(cost), directed=True)

    total_cost = min_cost[np.absolute(A)].T[1].astype(np.int64).sum()
    print(total_cost)

if __name__ == "__main__":
    main()
