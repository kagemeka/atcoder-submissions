import typing


def main() -> None:
    n = int(input())
    # use two stack
    s = input()

    left = [0]
    right = []
    for i, c in enumerate(s):
        if c == "L":
            right.append(left.pop())
            left.append(i + 1)
        else:
            left.append(i + 1)
    a = left + right[::-1]
    print(*a)


if __name__ == "__main__":
    main()
