import typing
import heapq

def main() -> None:
    n, k = map(int, input().split())
    p = list(map(int, input().split()))

    hq = []
    for i in range(k):
        heapq.heappush(hq, p[i])

    for i in range(k, n):
        print(hq[0])
        heapq.heappushpop(hq, p[i])
    print(hq[0])



main()
