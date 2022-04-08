import heapq


def main() -> None:
    n, m = map(int, input().split())

    g = [[] for _ in range(n)]
    in_deg = [0] * n
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        g[a].append(b)
        in_deg[b] += 1

    hq = []
    for i in range(n):
        if in_deg[i] > 0:
            continue
        heapq.heappush(hq, i)

    sequence = []
    while hq:
        i = heapq.heappop(hq)
        sequence.append(i)
        for j in g[i]:
            in_deg[j] -= 1
            if in_deg[j] == 0:
                heapq.heappush(hq, j)

    if len(sequence) != n:
        print(-1)
        return

    print(*map(lambda x: x + 1, sequence))


if __name__ == "__main__":
    main()
