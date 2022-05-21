import heapq


def main() -> None:
    n, l = map(int, input().split())
    a = list(map(int, input().split()))
    s = sum(a)
    if l > s:
        a.append(l - s)

    q = []
    for x in a:
        heapq.heappush(q, x)

    tot = 0
    for _ in range(len(a) - 1):
        cost = heapq.heappop(q) + heapq.heappop(q)
        tot += cost
        heapq.heappush(q, cost)

    print(tot)


if __name__ == "__main__":
    main()
