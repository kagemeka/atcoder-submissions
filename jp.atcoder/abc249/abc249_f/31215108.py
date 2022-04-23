def main() -> None:
    n, k = map(int, input().split())
    ops = [tuple(map(int, input().split())) for _ in range(n)]
    # fix last ops in t == 1.
    # if fix, skip all the latter ops t == 1.

    # for t == 2 after the last t == 1,
    # skip ops in ascending order of y greedly
    ops = [(1, 0)] + ops
    n += 1
    skipped = [False] * n
    stack = []
    remain = k
    dy_sum = 0
    for i in range(n):
        t, y = ops[i]
        if t == 1:
            skipped[i] = True
            remain -= 1
        else:
            stack.append((i, y))
            dy_sum += y
    stack.sort(key=lambda x: x[1], reverse=True)

    INF = 1 << 60
    mx = -INF
    for i in range(n):
        t, y = ops[i]
        if t == 1:
            skipped[i] = False
            remain += 1
            while remain > 0 and stack:
                while stack and stack[-1][0] < i:
                    stack.pop()
                if stack and stack[-1][1] < 0:
                    j, x = stack.pop()
                    remain -= 1
                    skipped[j] = True
                    dy_sum -= x
                else:
                    break
            if remain >= 0:
                mx = max(mx, y + dy_sum)
        else:
            if skipped[i]:
                skipped[i] = False
                remain += 1
            else:
                dy_sum -= y
    print(mx)


if __name__ == "__main__":
    main()
