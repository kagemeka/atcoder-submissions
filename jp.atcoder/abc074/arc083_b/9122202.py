import sys
import numpy as np
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix

'''
Aが最短距離を表す、というのはSnukeの推測でしかない。
なので、Aを、A[v, u]が辺の重みを表しているgraphとして捉え、floyd_warshallで実際に最短距離を求め、Bとする。

B[v, u] < A[v, u]が存在したらAが最短距離を表すという推測は間違っていたことになる。
もしB[v, u] == B[v, w] + B[w, u](ただし w ≠ v, w ≠ u)となるようなwが存在したら、
Aのgraphでedge(v, u)はなくても良いことになるので、A[v, u] = A[u, v] = 0として辺を消す。(仮に辺を消しても、shortest_dist(v, u)には影響しないため)

最後に残った辺々だけをつなげてできるグラフの合計の辺の重みが答えとなる
'''

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
