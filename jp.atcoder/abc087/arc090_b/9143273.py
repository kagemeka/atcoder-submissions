import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for l, r, d in zip(*[map(int, sys.stdin.read().split())] * 3):
    graph[l].append((r, d))
    graph[r].append((l, -d))

def main():
    dist = [None] * (n + 1)
    i = 1
    while i <= n:
        if dist[i] is not None:
            i += 1
            continue
        dist[i] = 0
        stack = [i]
        while stack:
            x = stack.pop()
            for y, d in graph[x]:
                if dist[y] is None:
                    dist[y] = dist[x] + d
                    stack.append(y)
                elif dist[y] != dist[x] + d:
                    return 'No'
    return 'Yes'

if __name__ == '__main__':
    ans = main()
    print(ans)
