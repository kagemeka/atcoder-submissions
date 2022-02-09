# 2019-11-26 01:21:13(JST)
import sys
import numpy as np

def main():
    H, W = map(int, sys.stdin.readline().split())
    visited = np.array([sys.stdin.readline().rstrip() + '.' for _ in range(H)], dtype='U')
    visited = np.append(visited, '.' * (W + 1))

    if np.char.count(visited, '#').sum() != H + W - 1:
        print('Impossible')
        sys.exit()

    h, w = 0, 0
    for _ in range(H + W - 2):
        if visited[h+1][w] == '#' and visited[h][w+1] == '.':
            h += 1
        elif visited[h+1][w] == '.' and visited[h][w+1] == '#':
            w += 1
        else:
            print('Impossible')

    print('Possible')


if __name__ == '__main__':
    main()
