def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))
    total_bugs = 0
    softwares_with_bugs = 0

    for x in a:
        total_bugs += x
        softwares_with_bugs += x > 0
    print((total_bugs + softwares_with_bugs - 1) // softwares_with_bugs)


if __name__ == "__main__":
    main()
