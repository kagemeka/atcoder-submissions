import itertools


def main() -> None:
    # floyd_warshall -> tsp for visiting nodes.
    n, m, r = map(int, input().split())
    visiting_nodes = list(map(int, input().split()))
    for i in range(r):
        visiting_nodes[i] -= 1

    INF = 1 << 60
    dist = [[INF] * n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        a -= 1
        b -= 1
        dist[a][b] = dist[b][a] = c
    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    min_dist = INF
    for perm in itertools.permutations(range(r)):
        a = [visiting_nodes[i] for i in perm]
        min_dist = min(
            min_dist,
            sum(dist[a[i]][a[i + 1]] for i in range(r - 1)),
        )
    assert min_dist != INF
    print(min_dist)


if __name__ == "__main__":
    main()
