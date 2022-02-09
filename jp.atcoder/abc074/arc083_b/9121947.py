import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix
from itertools import combinations


n = int(sys.stdin.readline().rstrip())
A = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n, n)

def main():
    B = floyd_warshall(A, directed=False)
    if np.any(A - B > 0):
        return -1

    will_subtract = []
    for v, u in combinations(range(n), 2):
        d = B[v, u]
        for w in range(n):
            if w != v and w != u:
                if B[v, w] + B[w, u] == d:
                    will_subtract.append(d)

    ans = np.sum(B) // 2 - sum(will_subtract)
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
