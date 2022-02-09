import sys
import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
a, b, c = I[2:].reshape(m, 3).T
a -= 1; b -= 1
graph = np.zeros((n, n))
graph[a, b] = c

def main():
    dist = floyd_warshall(csgraph=csr_matrix(graph), directed=False)
    bl =  (dist[:, a] == dist[:, b] + c) | (dist[:, b] == dist[:, a] + c)
    res = np.any(bl, axis=0)
    ans = m - np.count_nonzero(res)
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
