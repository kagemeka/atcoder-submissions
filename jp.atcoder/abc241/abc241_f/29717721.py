import collections
import bisect
import typing


def main() -> None:
    # BFS
    # nodes are at most 4N
    # edges are at most 8N
    # O(8N + 4N)

    h, w, n = map(int, input().split())
    sy, sx = map(lambda x: int(x) - 1, input().split())
    gy, gx = map(lambda x: int(x) - 1, input().split())
    yx = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]

    def on_grid(y: int, x: int) -> bool:
        return 0 <= y < h and 0 <= x < w

    objects = set(yx)
    dyx = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    node_ids = {(sy, sx): 0, (gy, gx): 1}
    for y, x in yx:
        for dy, dx in dyx:
            ny = y + dy
            nx = x + dx
            if not on_grid(ny, nx) or (ny, nx) in objects:
                continue
            node_ids[(ny, nx)] = node_ids.get((ny, nx), len(node_ids))

    # object coordinates
    y_lists = collections.defaultdict(list)
    x_lists = collections.defaultdict(list)
    for y, x in yx:
        y_lists[x].append(y)
        x_lists[y].append(x)

    m = len(node_ids)
    graph = [[] for _ in range(m)]

    for u, u_id in node_ids.items():
        y, x = u
        y_list = y_lists[x]
        i = bisect.bisect_left(y_list, y)
        if i < len(y_list):
            v = (y_list[i] - 1, x)
            assert v >= u
            v_id = node_ids[v]
            graph[u_id].append(v_id)
        i = bisect.bisect_right(y_list, y)
        if i > 0:
            v = (y_list[i - 1] + 1, x)
            assert v <= u
            v_id = node_ids[v]
            graph[u_id].append(v_id)
        x_list = x_lists[y]
        i = bisect.bisect_left(x_list, x)
        if i < len(x_list):
            v = (y, x_list[i] - 1)
            assert v >= u
            v_id = node_ids[v]
            graph[u_id].append(v_id)
        i = bisect.bisect_right(x_list, x)
        if i > 0:
            v = (y, x_list[i - 1] + 1)
            assert v <= u
            v_id = node_ids[v]
            graph[u_id].append(v_id)

    inf = 1 << 60
    dist = [inf] * m
    dist[0] = 0
    que = [0]
    for u in que:
        for v in graph[u]:
            dv = dist[u] + 1
            if dv >= dist[v]:
                continue
            dist[v] = dv
            que.append(v)

    print(-1 if dist[1] == inf else dist[1])


if __name__ == "__main__":
    main()
