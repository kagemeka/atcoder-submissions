import sys

n, m, *ab = map(int, sys.stdin.read().split())
graph = [set() for _  in range(n)]
for a, b in zip(*[iter(ab)] * 2):
    a -= 1; b -= 1
    graph[a].add(b); graph[b].add(a)

def main():
    stack = [i for i in range(n) if len(graph[i]) == 1]
    bridges = 0
    while stack:
        x = stack.pop()
        if not graph[x]: continue
        y = graph[x].pop()
        graph[y].remove(x)
        bridges += 1
        if len(graph[y]) == 1:
            stack.append(y)
    print(bridges)

if __name__ ==  '__main__':
    main()
