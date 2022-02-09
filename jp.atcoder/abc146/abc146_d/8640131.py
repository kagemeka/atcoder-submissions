# 2019-11-24 20:59:47(JST)
import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    m = map(int, sys.stdin.read().split())
    ab = list(zip(m, m)) # 2回以上使えるようにlist化

    graph = [[] for _ in range(n + 1)]
    for a, b in ab:
        graph[a].append(b)
        graph[b].append(a)

    root = 1
    parent = [None] * (n + 1)
    # treeなのでループがないため、parentが定義できる
    checked = []
    to_check = [root]
    # dfs: depth first search では stack
    # bfs: breadth first search では queueを使う
    # 今回は stack

    while to_check:
        x = to_check.pop()
        # stackから要素を取り除き、xにset
        for y in graph[x]: # xから直接つながっているverticesについて
            if y == parent[x]:
                continue
            # yがxの親でなければ
            parent[y] = x # xを親にして
            to_check.append(y) # 子であるyをto_checkにstackしていく
        checked.append(x) # 探索が終わったらvertexを記録

    color = [-1] * (n + 1) # 初期は0でもいいが、あえてngであることがわかりやすいように-1にしている
    for x in checked: # checkされた順になっている
        ng = color[x] # 最初は-1, colorは1からなので最初はngにはならない
        c = 1
        for y in graph[x]:
            if y == parent[x]:
                continue
            if c == ng:
                c += 1
            color[y] = c
            c += 1

    res = []
    for a, b in ab:
        if a == parent[b]:
            res.append(color[b])
        else: # 木なので parent[a] == b
            res.append(color[a])

    print(max(res))
    print('\n'.join(map(str, res)))


if __name__ == '__main__':
    main()
