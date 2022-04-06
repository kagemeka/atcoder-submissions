import typing
import heapq


def main() -> None:
    n, q = map(int, input().split())

    K = 1 << 18
    rate_queues = [[] for _ in range(K)]

    rate = [-1] * n
    belongs_to = [-1] * n
    for i in range(n):
        r, j = map(int, input().split())
        j -= 1
        belongs_to[i] = j
        rate[i] = r
        heapq.heappush(rate_queues[j], (-rate[i], i))

    evenness_queue = []

    def add_to_evenness_queue(j: int):
        rate_queue = rate_queues[j]
        while rate_queue:
            r, i = rate_queue[0]
            if belongs_to[i] == j:
                break
            heapq.heappop(rate_queue)
        if not rate_queue:
            return
        r, i = rate_queue[0]
        r = -r
        heapq.heappush(evenness_queue, (r, i, j))

    for j in range(K):
        add_to_evenness_queue(j)

    for _ in range(q):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        prev = belongs_to[i]
        belongs_to[i] = j
        heapq.heappush(rate_queues[j], (-rate[i], i))
        add_to_evenness_queue(j)

        add_to_evenness_queue(prev)

        while evenness_queue:
            r, i, j = evenness_queue[0]
            if belongs_to[i] == j and r == -rate_queues[j][0][0]:
                break
            heapq.heappop(evenness_queue)
        assert evenness_queue

        print(evenness_queue[0][0])


if __name__ == "__main__":
    main()
