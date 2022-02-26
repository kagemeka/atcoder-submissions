import collections


def main() -> None:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    cnt_a = collections.Counter(a)
    cnt_b = collections.Counter(b)
    for v, c in cnt_b.items():
        if cnt_a[v] < c:
            print("No")
            return
    print("Yes")


if __name__ == "__main__":
    main()
