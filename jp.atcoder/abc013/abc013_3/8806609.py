import sys
import numpy as np

n, h, a, b, c, d, e = map(int, sys.stdin.read().split())

def cost(x, y):
    return a * x + c * y

def main():
    x = np.arange(n+1, dtype=np.int64)
    y = (n * e - (b + e) * x - h + (d + e)) // (d + e)
    y = np.maximum(y, 0) # マイナス日食べることはできない
    y = np.minimum(y, n - x) # xを固定した時にx+y(x+y >= n+1)日以上食べ続けないと体調を崩す場合でも、n日までのことだけを考えれば良い。

    costs = cost(x, y)
    return np.amin(costs)

if __name__ == '__main__':
    ans = main()
    print(ans)
