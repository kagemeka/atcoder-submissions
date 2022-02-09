import sys

h, w = map(int, sys.stdin.readline().split())
canvas = ['.' * (w + 2)]
canvas += ['.' + sys.stdin.readline().rstrip() + '.' for _ in range(h)]
canvas += ['.' * (w + 2)]

def main():
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for i in range(1, h+1):
        for j in range(1, w+1):
            if canvas[i][j] == '#':
                for di, dj in d:
                    y = i + di
                    x = j + dj
                    if canvas[y][x] == '#':
                        break
                else:
                    return 'No'
    return 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)
