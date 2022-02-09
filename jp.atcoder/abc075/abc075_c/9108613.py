import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
ab = map(int, sys.stdin.read().split())
ab = zip(*[ab] * 2)
graph = [set() for _ in range(n+1)]
for a, b in ab:
    graph[a].add(b)
    graph[b].add(a)

def main():
    que = set()
    for i in range(1, n+1):
        if len(graph[i]) == 1:
            que.add(i)
    res = len(que)
    while que:
        x = que.pop()
        y = graph[x].pop()
        graph[y] -= set([x])
        l = len(graph[y])
        if l == 0:
            que -= set([y])
            res -= 1
        elif l == 1:
            que.add(y)
            res += 1

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
