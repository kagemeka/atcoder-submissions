import sys

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def main():
    to_check = set(range(1, n+1))
    checked = set()
    cnt = 0
    while to_check:
        queue = set([to_check.pop()])
        cnt += 1
        while queue:
            v = queue.pop()
            checked.add(v)
            to_check -= set([v])
            for u in graph[v]:
                if not u in checked:
                    queue.add(u)
    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
