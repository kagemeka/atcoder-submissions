import sys

n, *ab = map(int, sys.stdin.read().split())
graph = [[]for _ in range(n+1)]
for a, b in zip(*[iter(ab)] * 2):
    graph[a].append(b)
    graph[b].append(a)

def dfs(v):
    stack = [v]
    dist = [None] * (n + 1)
    dist[v] = 0
    while stack:
        x = stack.pop()
        for y in graph[x]:
            if dist[y] is None:
                dist[y] = dist[x] + 1
                stack.append(y)
    return dist

def main():
    dist_1 = dfs(1)
    dist_n = dfs(n)
    black_cnt = 0
    for i in range(1, n+1):
        if dist_1[i] <= dist_n[i]:
            black_cnt += 1

    if black_cnt <= n // 2:
        return 'Snuke'
    else:
        return 'Fennec'

if __name__ == '__main__':
    ans = main()
    print(ans)
