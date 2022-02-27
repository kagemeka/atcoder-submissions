def main() -> None:
    n = int(input())
    # greedy
    # slide to right
    # O(N^2)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a = a[::-1]
    b = b[::-1]
    # a b c -> b c a (because reversed)
    for i in range(n):
        if a[i] == b[i]:
            continue

        try:
            j = a.index(b[i], i + 1)
            a[i + 1 : j + 1] = a[i:j]
            a[i] = b[i]
        except:
            print("No")
            return
    print("Yes")


main()
