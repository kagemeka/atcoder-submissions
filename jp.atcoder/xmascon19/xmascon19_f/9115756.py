import sys

h, w = map(int, sys.stdin.readline().split())
grid = sys.stdin.read().split()

def main():
    res = 0

    for i in range(h):
        if '.' in grid[i]:
            yu = i
            break
    else:
        return 0

    yb = min(yu + h // 2, h)

    x = set()
    for i in range(yu, yb):
        for j in range(w):
            if grid[i][j] == '.':
                x.add(j)
    x = sorted(x)
    res += ((x[-1] - x[0] + 1) + w // 2 - 1) // (w // 2)

    x = set()
    for i in range(yb, h):
        for j in range(w):
            if grid[i][j] == '.':
                x.add(j)
    if not x:
        return res
    x = sorted(x)
    res += ((x[-1] - x[0] + 1) + w // 2 - 1) // (w // 2)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
