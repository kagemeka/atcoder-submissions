import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[False] * n for _ in range(n)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    x -= 1; y -= 1
    graph[x][y] = graph[y][x] = True

def main():
    res = 1
    for i in range(1 << n):
        comb = [j for j in range(n) if i >> j & 1]
        m = len(comb)
        for j in range(m - 1):
            for k in range(j + 1, m):
                if not graph[comb[j]][comb[k]]: break
            else: continue
            break
        else:
            res = max(res, m)
    print(res)

if __name__ ==  '__main__':
    main()
