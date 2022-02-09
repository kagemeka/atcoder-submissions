import sys

h, w = map(int, sys.stdin.readline().split())
canvas = ['.' * (w + 2)] + ['.' + sys.stdin.readline().rstrip() + '.' for _ in range(h)] + ['.' * (w + 2)]


def main():
    res = [[0] * (w + 1) for _ in range(h + 1)]
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if canvas[i][j] == '#':
                res[i][j] = '#'
                continue
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    y = i + di
                    x = j + dj
                    if canvas[y][x] == '#':
                        res[i][j] += 1

    for i in range(1, h+1):
        yield ''.join(list(map(str, res[i][1:])))

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
