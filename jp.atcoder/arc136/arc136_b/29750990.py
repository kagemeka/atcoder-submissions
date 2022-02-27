def main() -> None:
    n = int(input())
    # greedy
    # slide to right
    # O(N^2)
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    # a = a[::-1]
    # b = b[::-1]
    # a b c -> b c a (because reversed)

    # odd or even
    # for i in range(n):
    #     if a[i] == b[i]:
    #         continue
    #     # print(i)
    #     try:
    #         # j = a.index(b[i], i + 1)
    #         j = n - 1 - a[::-1].index(b[i])
    #         if j < i:
    #             raise
    #         # print(j, i)
    #         if (j - i) % 2 == 0:
    #             a[i + 1 : j + 1] = a[i:j]
    #             a[i] = b[i]
    #             # print(a)
    #         else:
    #             a[i + 2 : j + 1] = a[i + 1 : j]
    #             if i + 1 == n - 1:
    #                 print("No")
    #                 return
    #             a[i], a[i + 1], a[i + 2] = b[i], a[i + 2], a[i]

    #             # a[i + 1] = b[i]

    #     except:
    #         print("No")
    #         return
    # print("Yes")
    for i in range(n):
        if a[i] == b[i]:
            continue
        if i >= n - 2:
            print("No")
            return
        flg = False
        for j in range(i + 2, n, 2):
            if a[j] == b[i]:
                a[i + 1 : j + 1] = a[i:j]
                a[i] = b[i]
                flg = True
                break
        if flg:
            continue
        for j in range(i + 3, n, 2):
            if a[j] == b[i]:
                a[i + 2 : j + 1] = a[i + 1 : j]
                a[i + 1] = b[i]
                # a[i], a[i + 2] = b[i], a[i]
                # flg = True
                break
        if a[i + 1] == b[i]:
            a[i], a[i + 1], a[i + 2] = b[i], a[i + 2], a[i]
            continue
        print("No")
        return
    print("Yes")
    # if flg:
    #     continue


main()
