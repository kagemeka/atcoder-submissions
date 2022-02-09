import sys
import numpy as np

n = int(sys.stdin.readline().rstrip())
txy = np.array(sys.stdin.read().split(), dtype=np.int64).reshape(n, 3)
t, x, y = np.concatenate((np.array([[0, 0, 0]]), txy), axis=0).T

def main():
    dt = t[1:] - t[:-1]
    dd = np.absolute(x[1:] - x[:-1]) + np.absolute(y[1:] - y[:-1])
    ans = 'Yes' if np.all((dt >= dd) & (dt & 1 == dd & 1)) else 'No'
    print(ans)

if __name__ ==  '__main__':
    main()
