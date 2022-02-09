import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

I = np.array(sys.stdin.read().split(), dtype=np.int64)
h, w = I[:2]
c = I[2:102].reshape(10, 10)
a = I[102:].reshape(h, w)

def main():
    cost = floyd_warshall(csr_matrix(c), directed=True).astype(np.int64)

    res = cost[a[a != -1], 1]
    return np.sum(res)

if __name__ == '__main__':
    ans = main()
    print(ans)
