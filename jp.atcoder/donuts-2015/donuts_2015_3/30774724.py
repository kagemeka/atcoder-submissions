def main() -> None:
    # use stack
    # online

    n = int(input())
    h = list(map(int, input().split()))

    stack = []
    for x in h:
        print(len(stack))
        while stack and stack[-1] <= x:
            stack.pop()
        stack.append(x)


if __name__ == "__main__":
    main()
