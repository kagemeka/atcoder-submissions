import typing
import heapq


def main() -> typing.NoReturn:
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    # count mn ...(k - 1)... mx
    # count i, i + 1, i + 2, ... i + k - 1
    # be careful of duplicates.

    to_remove = [True] * n

    # 1. lazy min heap and max heap
    # 2. segment tree
    # 3. set (binary search tree)


    mn_hq = []
    mx_hq = []

    for i, x in enumerate(p):
        while mn_hq and mn_hq[0][1] < i - k:
            heapq.heappop(mn_hq)

        if mn_hq:
            to_remove[i] &= mn_hq[0][1] == i - k
        else:
            to_remove[i] = False

        heapq.heappush(mn_hq, (x, i))

        while mx_hq and mx_hq[0][1] <= i - k:
            heapq.heappop(mx_hq)
        if mx_hq:
            to_remove[i] &= -mx_hq[0][0] < x
        else:
            to_remove[i] = False

        heapq.heappush(mx_hq, (-x, i))



    asc_appeared = False
    cnt = 1
    for i in range(n - 1):
        if p[i + 1] < p[i]:
            cnt = 1
            continue
        cnt += 1
        if cnt < k: continue
        if asc_appeared:
            to_remove[i + 1] |= True
        else:
            asc_appeared = True

    ans = n - k + 1 - sum(to_remove)
    print(ans)


main()
