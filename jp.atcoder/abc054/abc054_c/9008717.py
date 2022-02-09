import sys

n, m = map(int, sys.stdin.readline().split())
ab = map(int, sys.stdin.read().split())
ab = zip(*[ab] * 2)
graph = [[] for _ in range(n)]
for a, b in ab:
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def main():

    cnt = 0
    stack = [(0, set())]
    while stack:
        v, visited = stack.pop()
        visited.add(v)
        if len(visited) == n:
            cnt += 1
            continue
        for u in graph[v]:
            if u in visited:
                continue
            stack.append((u, visited.copy()))

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
