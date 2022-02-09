import sys

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u-1].append((v - 1, w))
    graph[v-1].append((u - 1, w))

def coloring_tree(g, size):
    par = [None] * size
    stack = [(0, 0)]
    color = [None] * size
    color[0] = 0
    while stack:
        u, d = stack.pop()
        color[u] = d & 1
        for v, w in g[u]:
            if par[u] == v:
                continue
            par[v] = u
            stack.append((v, d + w))
    return color

def main():
    return coloring_tree(graph, n)

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
