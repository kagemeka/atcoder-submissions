# mypy: ignore-errors


def main() -> None:
    n = int(input())

    # binary lifting

    # at first, compute all dist from arbitrary root (r:= 3)
    # then, binary search node u path_3,2 or path_3,1

    # d_3,1 + d_3,2 - d_3,u * 2 = d_u,1 + d_u,2

    def query(u: int, v: int) -> int:
        print(f"? {u} {v}", flush=True)
        return int(input())

    root = 3
    dist = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == root:
            continue
        dist[i] = query(root, i)

    ok_dep = 0
    ok_node = root
    ng_dep = max(dist[1], dist[2])
    u = 1 if dist[1] == ng_dep else 2
    v = 3 - u

    dep_nodes = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        dep_nodes[dist[i]].append(i)

    du, dv = dist[u], dist[v]  # for assert
    rem = n + 1
    while ng_dep - ok_dep > 1:
        dep = (ok_dep + ng_dep) >> 1

        flg = False
        # ok = False
        for x in dep_nodes[dep]:
            if x == v:
                flg = True
                continue
            assert rem > 0
            rem -= 1
            du = query(u, x)
            if du + dist[x] > dist[u]:
                continue
                # not on path root-u

            assert rem > 0
            rem -= 1
            dv = query(v, x)
            if dist[u] + dist[v] - 2 * dist[x] == du + dv:
                ok_dep = dep
                ok_node = x
            else:
                ng_dep = dep
            break
        else:
            if flg:
                ok_dep = dep
                ok_node = v
                dv = 0
                du = dist[u] - dist[v]
                break
            else:
                ng_dep = dep

    ans = dist[u] + dist[v] - 2 * dist[ok_node]
    # assert ans == du + dv
    print(f"! {ans}", flush=True)


main()
