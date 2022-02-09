import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

n = int(sys.stdin.readline().rstrip())
A = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n, n)

def main():
    B = floyd_warshall(csr_matrix(A), directed=False).astype(np.float64)
    if np.any(B < A):
        return -1

    np.fill_diagonal(B, np.inf)

    for v in range(n-1):
        for u in range(v+1, n):
            detours = B[v] + B[u]
            if np.any(detours == B[v, u]):
                A[v, u] = A[u, v] = 0

    return np.sum(A) // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
