# 2019-11-26 01:21:13(JST)
import sys
import numpy as np

def main():
    H, W = map(int, sys.stdin.readline().split())
    visited = np.array([sys.stdin.readline().rstrip() for _ in range(H)], dtype='U')

    if np.char.count(visited, '#').sum() == H + W - 1:
        ans = 'Possible'
    else:
        ans = 'Impossible'

    print(ans)

if __name__ == '__main__':
    main()
