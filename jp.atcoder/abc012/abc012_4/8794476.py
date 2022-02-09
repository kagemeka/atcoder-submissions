import sys
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import floyd_warshall
import numpy as np

n, m = map(int, sys.stdin.readline().split())
I = map(int, sys.stdin.read().split())
abt = list(zip(I, I, I))

def main():
    G = [[0] * n for _ in range(n)]

    for a, b, t in abt:
        G[a-1][b-1] = t
        G[b-1][a-1] = t

    dist = floyd_warshall(csgraph=csr_matrix(G), directed=False)

    ans = np.amin(np.amax(dist, axis=1))
    print(ans)

if __name__ == '__main__':
    main()
