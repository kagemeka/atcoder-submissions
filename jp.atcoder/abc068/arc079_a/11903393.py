import sys

n, m, *ab = map(int, sys.stdin.read().split())
graph = [set() for _ in range(n + 1)]
for a, b in zip(*[iter(ab)] * 2):
    graph[a].add(b); graph[b].add(a)

def main():
    ans = 'IMPOSSIBLE'
    for x in graph[1]:
        if n in graph[x]:
            ans = 'POSSIBLE'
            break
    print(ans)

if __name__ ==  '__main__':
    main()
