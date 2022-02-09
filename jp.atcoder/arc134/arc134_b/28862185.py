import typing
import heapq


def main() -> None:
    n = int(input())
    s = list(input())
    hq = []
    for i, c in enumerate(s):
        heapq.heappush(hq, (c, -i))

    mn_right = n
    for i in range(n):
        if i >= mn_right:
            break
        while hq and -hq[0][1] <= i:
            heapq.heappop(hq)
        if not hq:
            break
        c, j = heapq.heappop(hq)
        j *= -1
        if j >= mn_right or c >= s[i]:
            heapq.heappush(hq, (c, -j))
            continue
        assert i < j < mn_right
        s[i], s[j] = s[j], s[i]
        mn_right = j
    print("".join(s))


if __name__ == "__main__":
    main()
