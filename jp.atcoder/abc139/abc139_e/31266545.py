def main() -> None:
    n = int(input())
    # bfs

    stacks = [list(map(lambda x: int(x) - 1, input().split()))[::-1] for _ in range(n)]

    que = []
    for i in range(n):
        j = stacks[i][-1]
        if j < i:
            continue
        if stacks[j][-1] == i:
            que.append(i)
            que.append(j)

    days = 0
    while que:
        days += 1
        next_que = []
        for i in que:
            stacks[i].pop()
            if not stacks[i]:
                continue
            j = stacks[i][-1]
            if not stacks[j] or stacks[j][-1] != i:
                continue
            next_que.append(i)
            next_que.append(j)
        que = next_que
    print(days if all(not s for s in stacks) else -1)


if __name__ == "__main__":
    main()
