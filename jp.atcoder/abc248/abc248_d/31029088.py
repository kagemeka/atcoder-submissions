def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    # [(l - 1, x, query_index), (r, x, query_index), ...]

    q = int(input())

    queries = [tuple(map(int, input().split())) for _ in range(q)]

    result = [0] * q
    check_count = [0] * q

    target = [0] * q
    queue = []
    for i in range(q):
        l, r, x = queries[i]
        l -= 1
        r -= 1
        target[i] = x
        queue.append((l - 1, i))
        queue.append((r, i))

    queue.sort()
    stack = queue[::-1]

    count = [0] * (n + 1)
    while stack and stack[-1][0] == -1:
        j, k = stack.pop()
        if check_count[k] == 1:
            result[k] = count[target[k]] - result[k]
        else:
            result[k] = count[target[k]]
        check_count[k] += 1

    for i in range(n):
        count[a[i]] += 1
        while stack and stack[-1][0] == i:
            j, k = stack.pop()
            if check_count[k] == 1:
                result[k] = count[target[k]] - result[k]
            else:
                result[k] = count[target[k]]
            check_count[k] += 1
    print(*result, sep="\n")


if __name__ == "__main__":
    main()
