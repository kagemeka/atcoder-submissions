import string
import typing
import heapq


def main() -> None:
    # count '...AARCC...'
    n = int(input())
    s = input()
    counts = []
    for i in range(n):
        if s[i] != "R":
            continue
        j = 0
        while True:
            j += 1
            if i - j < 0 or i + j >= n:
                break
            if not (s[i - j] == "A" and s[i + j] == "C"):
                break
        j -= 1
        if j == 0:
            continue
        counts.append(j)

    popped = set()
    min_q = [(counts[i], i) for i in range(len(counts))]
    max_q = [(-counts[i], i) for i in range(len(counts))]

    heapq.heapify(min_q)
    heapq.heapify(max_q)
    # l = 0
    for i in range(n):
        if i & 1 == 0:
            while max_q and max_q[0][1] in popped:
                heapq.heappop(max_q)
            if not max_q:
                break
            c, j = heapq.heappop(max_q)
            c *= -1
            assert c > 0
            c -= 1
            if c > 0:
                heapq.heappush(max_q, (-c, j))
                heapq.heappush(min_q, (c, j))
            else:
                popped.add(j)
        else:
            while min_q and min_q[0][1] in popped:
                heapq.heappop(min_q)
            if not min_q:
                break

            c, j = heapq.heappop(min_q)
            popped.add(j)

    print(i)


if __name__ == "__main__":
    main()
