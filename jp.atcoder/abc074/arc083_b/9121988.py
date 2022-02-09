import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

n = int(sys.stdin.readline().rstrip())
A = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n, n)

def main():
    B = floyd_warshall(csr_matrix(A), directed=False)
    if np.any(A - B > 0):
        return -1

    will_subtract = []
    for v in range(n-1):
        for u in range(v+1, n):
            d = B[v, u]
            for w in range(v):
                if B[v, w] + B[w, u] == d:
                    will_subtract.append(d)
                    break
            else:
                for w in range(v+1, u):
                    if B[v, w] + B[w, u] == d:
                        will_subtract.append(d)
                        break
                else:
                    for w in range(u+1, n):
                        if B[v, w] + B[w, u] == d:
                            will_subtract.append(d)
                            break

    ans = np.sum(B) // 2 - sum(will_subtract)
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
