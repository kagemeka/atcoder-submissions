import sys
from itertools import product

h, w = map(int, sys.stdin.readline().split())
s = ['#' * (w + 2)] + ['#' + sys.stdin.readline().rstrip() + '#' for _ in range(h)] + ['#' * (w + 2)]

def main():
    dij = list(product([-1, 0, 1], repeat=2))
    for i in range(h+2):
        print(s[i])
    cand = set()
    to_be_black = set()
    for i in range(1, h+1):
        for j in range(1, w+1):
            inside = set()
            for di, dj in dij:
                y = i + di
                x = j + dj
                if s[y][x] == '#':
                    inside.add((y, x))
                else:
                    break
            else:
                if len(inside) == 9:
                    cand.add((i, j))
                    to_be_black |= inside

    for i in range(1, h+1):
        for j in range(1, w+1):
            if s[i][j] == '#' and not (i, j) in to_be_black:
                print('impossible')
                sys.exit()

    yield 'possible'
    res = [['.'] * w for _ in range(h)]
    for i, j in cand:
        res[i-1][j-1] = '#'

    for i in range(h):
        yield ''.join(res[i])

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
