def main() -> None:
    # greedy

    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    stack = sorted(set(range(1, n + 1)) - set(a), reverse=True)
    sections = [[] for _ in range(k + 1)]

    for i in range(k):
        if not stack:
            break
        if stack[-1] < a[i]:
            sections[i + 1].append(stack.pop())

    while stack and stack[-1] < a[-1]:
        sections[-1].append(stack.pop())

    while stack:
        sections[-2].append(stack.pop())

    p = sorted(sections[0], reverse=True)
    for i in range(k):
        p.append(a[i])
        p += sorted(sections[i + 1], reverse=True)
    print(*p)


if __name__ == "__main__":
    main()
