import sys
import numpy as np

n, *xy = map(int, sys.stdin.read().split())
x, y = np.array(xy).reshape(-1, 2).T

def main():
    dx = (x[:, None] - x) ** 2
    dy = (y[:, None] - y) ** 2
    ans = np.sqrt(dx + dy).sum() / n
    print(ans)

if __name__ ==  '__main__':
    main()
