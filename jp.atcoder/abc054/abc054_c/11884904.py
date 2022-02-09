import sys

n, m, *ab = map(int, sys.stdin.read().split())
graph = [[] for _ in range(n)]
for a, b in zip(*[iter(ab)] * 2):
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)

def main():
    stack = [(0, 0)]
    paths = 0
    while stack:
        i, visited = stack.pop()
        visited |= 1 << i
        if visited == (1 << n) - 1:
            paths += 1
            continue
        for j in graph[i]:
            if visited >> j & 1: continue
            stack.append((j, visited))
    print(paths)

if __name__ ==  '__main__':
    main()
