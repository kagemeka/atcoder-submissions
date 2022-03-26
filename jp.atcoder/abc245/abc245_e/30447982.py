import heapq


def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))

    # heap
    # manage y in heap
    # 1. primary key: x (ascending)
    # 2. secondary key: y (descending)

    xy = sorted(zip(a, b), key=lambda p: p[0])
    ab = sorted(zip(c, d), key=lambda p: (p[0], -p[1]))

    hq = []
    i = 0
    for a, b in ab:
        while i < n and xy[i][0] <= a:
            y = xy[i][1]
            heapq.heappush(hq, -y)
            i += 1
        if not hq or -hq[0] > b:
            continue
        heapq.heappop(hq)

    if i != n or hq:
        print("No")
        return
    print("Yes")


if __name__ == "__main__":
    main()
