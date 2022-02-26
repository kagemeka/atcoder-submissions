def main() -> None:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    x = 0
    b = [(i + a[i]) % n for i in range(n)]  # next

    order = [-1] * n
    # order[0] = 0
    # appeared = [False] * n
    # appeared[x] = True
    sequence = []
    for i in range(n):
        order[x] = i
        sequence.append(x)
        x = b[x]
        if order[x] == -1:
            continue
        loop_size = i + 1 - order[x]
        first = x
        break
    else:
        raise

    cnt = 0
    x = 0
    while x != first and k:
        cnt += a[x]
        k -= 1
        x = b[x]
    if not k:
        print(cnt)
        return
    loop_sequence = sequence[order[first] :]
    # print(loop_sequence, loop_size)
    assert len(loop_sequence) == loop_size
    q, r = divmod(k, loop_size)
    cnt += q * sum(a[x] for x in loop_sequence)
    for i in range(r):
        cnt += a[loop_sequence[i]]
    print(cnt)


if __name__ == "__main__":
    main()
