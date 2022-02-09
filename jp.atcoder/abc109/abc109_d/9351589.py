import sys

h, w = map(int, sys.stdin.readline().split())
grid = [[int(x) for x in sys.stdin.readline().split()] for _ in range(h)]

def main():
    n = 0
    move = []

    for i in range(h):
        for j in range(w-1):
            if grid[i][j] & 1:
                grid[i][j] -= 1
                grid[i][j+1] += 1
                move.append((i+1, j+1, i+1, j+2))
                n += 1

    for i in range(h-1):
        if grid[i][-1] & 1:
            grid[i][-1] -= 1
            grid[i+1][-1] += 1
            move.append((i+1, w, i+2, w))
            n += 1

    yield [n]
    for m in move:
        yield m

if __name__ == '__main__':
    ans = main()
    for i in ans:
        print(*i, sep=' ')
