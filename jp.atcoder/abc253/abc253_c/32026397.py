import heapq
import typing
import collections


def main() -> None:
    q = int(input())

    max_q = []
    min_q = []

    cnt = collections.Counter()
    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x = query[1]
            cnt[x] += 1
            if cnt[x] == 1:
                heapq.heappush(max_q, -x)
                heapq.heappush(min_q, x)
            continue
        if query[0] == 2:
            x, c = query[1], query[2]
            cnt[x] -= min(cnt[x], c)
            continue
        while cnt[-max_q[0]] == 0:
            heapq.heappop(max_q)
        while cnt[min_q[0]] == 0:
            heapq.heappop(min_q)
        print(-max_q[0] - min_q[0])


if __name__ == "__main__":
    main()
