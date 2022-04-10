import collections


def main() -> None:
    n = int(input())
    count = collections.Counter()

    st = [input().split() for _ in range(n)]
    for s, t in st:
        count[s] += 1
        count[t] += 1

    for s, t in st:
        if count[s] >= 2 and count[t] >= 2:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
