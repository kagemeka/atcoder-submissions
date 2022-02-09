import typing


def main() -> typing.NoReturn:
    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    b = list(map(lambda x: int(x) - 1, input().split()))

    cnt = [0] * n
    for x in a:
        cnt[x] += 1
    loop = 0
    ptr = 0
    res = []
    for x in b:
        while loop * n + ptr <= x:
            ptr += 1
            if ptr == n:
                loop += 1
                ptr = 0
        while cnt[ptr] == 0:
            ptr += 1
            if ptr == n:
                ptr = 0
                loop += 1
        if ptr == x:
            print('No')
            return
        res.append(ptr)
        cnt[ptr] -= 1

    ptrs = [n] * n
    for i in range(n):
        if ptrs[a[i]] == n:
            ptrs[a[i]] = i
    ans = [-1] * n
    for i in range(n):
        ans[ptrs[res[i]]] = b[i] + 1
        ptrs[res[i]] += 1
    print('Yes')
    print(*ans)


main()
