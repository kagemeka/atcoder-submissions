import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

n = int(sys.stdin.readline().rstrip())
A = np.array(sys.stdin.read().split(), dtype=np.float64).reshape(n, n)

def main():
    B = floyd_warshall(csr_matrix(A), directed=False).astype(np.int64)
    if np.any(B < A):
        return -1

    np.fill_diagonal(A, np.inf)

    total_length = 0
    for v in range(n-1):
        for u in range(v+1, n):
            detours = A[v] + A[u]
            if np.all(detours > B[v, u]):
                total_length += B[v, u]

    return total_length

if __name__ == '__main__':
    ans = main()
    print(ans)
