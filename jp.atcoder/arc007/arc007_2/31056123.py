def main() -> None:
    n, m = map(int, input().split())

    disk = list(range(n + 1))  # what disk in case_i
    case = list(range(n + 1))  # in what case is dist_i

    for _ in range(m):
        i = int(input())
        case[disk[0]] = case[i]
        disk[case[i]] = disk[0]
        case[i] = 0
        disk[0] = i
    print(*disk[1:], sep="\n")


if __name__ == "__main__":
    main()
