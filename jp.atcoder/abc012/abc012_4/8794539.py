import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, m = I[:2]
abt = I[2:].reshape(-1, 3)

def main():
    G = np.zeros((n, n))

    for a, b, t in abt:
        G[a-1][b-1] = t
        G[b-1][a-1] = t

    dist = floyd_warshall(csgraph=csr_matrix(G), directed=False)

    ans = np.amin(np.amax(dist, axis=1))
    print(ans)

if __name__ == '__main__':
    main()
