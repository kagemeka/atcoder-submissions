def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    left = [-1] * n
    right = [-1] * n
    stack = [(-1, -1)]  # (height, index)

    for i in range(n):
        while stack[-1][0] >= a[i]:
            stack.pop()
        assert stack
        left[i] = stack[-1][1]
        stack.append((a[i], i))

    stack = [(-1, n)]
    for i in range(n - 1, -1, -1):
        while stack[-1][0] >= a[i]:
            stack.pop()
        assert stack
        right[i] = stack[-1][1]
        stack.append((a[i], i))

    print(max(a[i] * (right[i] - left[i] - 1) for i in range(n)))


if __name__ == "__main__":
    main()
