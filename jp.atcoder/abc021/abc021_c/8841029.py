import sys
import numpy as np

MOD = 10 ** 9 + 7

I = np.array(sys.stdin.read().split(), dtype=np.int64)
n, a, b, m = I[:4]
a -= 1; b -= 1
x, y = I[4:].reshape(-1, 2).T
G = np.zeros((n, n), dtype=np.int64)
G[x-1, y-1] = G[y-1, x-1] = 1

def main():
    res = np.zeros(n, dtype=np.int64).reshape(-1, 1)
    res[a, 0] = 1
    while not res[b, 0]:
        res = np.dot(G, res)
        res %= MOD
    '''
    c回ループしたときのresは、c回移動したとき、各頂点にいる場合の数を記録。
    各頂点vについて、初めてres[v] > 0となったときのcがaからvへの最小コストであり、
    そのときのres[v]がaからvへの最短経路の数である。
    今回はコストを記録する必要はない。
    '''
    return res[b, 0]

if __name__ == '__main__':
    ans = main()
    print(ans)
