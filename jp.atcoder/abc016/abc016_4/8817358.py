import sys
import numpy as np

I = np.array(sys.stdin.read().split(), dtype=np.int64)
xs, ys, xg, yg, n = I[:5]
a = (xs, ys)
b = (xg, yg)
xy1 = I[5:].reshape(-1, 2)
xy2 = np.append(xy1[1:], [xy1[0]], axis=0)
c = xy1.T
d = xy2.T

def are_crossed_ab_cd(a, b, c, d):
    t1 = (a[0] - b[0]) * (c[1] - a[1]) + (a[1] - b[1]) * (a[0] - c[0])
    t2 = (a[0] - b[0]) * (d[1] - a[1]) + (a[1] - b[1]) * (a[0] - d[0])
    t3 = (c[0] - d[0]) * (a[1] - c[1]) + (c[1] - d[1]) * (c[0] - a[0])
    t4 = (c[0] - d[0]) * (b[1] - c[1]) + (c[1] - d[1]) * (c[0] - b[0])
    return np.logical_and(t1 * t2 < 0, t3 * t4 < 0)

def main():
    res = are_crossed_ab_cd(a, b, c, d)
    return np.count_nonzero(res) // 2 + 1

if __name__ == '__main__':
    ans = main()
    print(ans)
