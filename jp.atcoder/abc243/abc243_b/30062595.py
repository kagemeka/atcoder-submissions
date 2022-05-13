def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    both = len(set(a) & set(b))
    same = 0
    for i in range(n):
        same += a[i] == b[i]

    different = both - same
    print(same)
    print(different)


if __name__ == "__main__":
    main()
