def main() -> None:
    q = int(input())

    # at first process all insertions.

    queries = [tuple(map(int, input().split())) for _ in range(q)]

    que = []
    for query in queries:
        if query[0] == 2:
            continue
        x, c = query[1:]
        que.append((x, c))

    que.reverse()

    for query in queries:
        if query[0] == 1:
            continue
        count = query[1]

        s = 0
        while True:
            x, c = que.pop()
            if count > c:
                count -= c
                s += x * c
                continue
            c -= count
            s += x * count
            que.append((x, c))
            break
        print(s)


if __name__ == "__main__":
    main()
