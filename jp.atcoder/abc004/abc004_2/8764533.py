import sys

grid = [sys.stdin.readline().split() for _ in range(4)]
res = []
for i in range(3, -1, -1):
    res.append(' '.join(list(reversed(grid[i]))))

def main():
    for i in range(4):
        print(res[i])

if __name__ == '__main__':
    main()
