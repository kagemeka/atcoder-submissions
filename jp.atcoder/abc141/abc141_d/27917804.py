import typing
import heapq

def main() -> typing.NoReturn:
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    hq = []
    for x in a:
        heapq.heappush(hq, -x)

    for _ in range(m):
        x = -heapq.heappop(hq)
        heapq.heappush(hq, -(x >> 1))


    print(-sum(hq))


main()
