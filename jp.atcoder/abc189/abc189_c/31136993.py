def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    # max right from leftmost position which count is less than the self one.
    # min left from rightmost position which count is less than the self one.

    left = [-1] * n
    right = [-1] * n

    stack = [(-1, 0)]
    for i in range(n):
        while stack[-1][1] >= a[i]:
            stack.pop()
        left[i] = stack[-1][0]
        stack.append((i, a[i]))

    stack = [(n, 0)]
    for i in range(n - 1, -1, -1):
        while stack[-1][1] >= a[i]:
            stack.pop()
        right[i] = stack[-1][0]
        stack.append((i, a[i]))

    print(max(a[i] * (right[i] - left[i] - 1) for i in range(n)))


if __name__ == "__main__":
    main()
