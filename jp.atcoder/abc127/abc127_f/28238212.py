import typing
import heapq

def main() -> typing.NoReturn:
    # median
    # multiset
    # find k-th element
    # two priority queue
    ...
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]

    hq1 = [] # get max
    hq2 = [] # get min
    _, a, b = queries[0]
    queries = queries[1:]
    s = b

    heapq.heappush(hq1, -a)

    for query in queries:
        if query[0] == 2:
            x = -hq1[0]
            print(x, s)
            continue

        a, b = query[1:]
        s += b
        n, m = len(hq1), len(hq2)
        x = -hq1[0]
        if n == m:
            # nx >= x
            if a <= hq2[0]:
                heapq.heappush(hq1, -a)
                nx = max(x, a)
            else:
                heapq.heappush(
                    hq1,
                    -heapq.heappushpop(hq2, a),
                )
                nx = -hq1[0]
        else:
            # nx <= x
            if a >= x:
                heapq.heappush(hq2, a)
                nx = x
            else:
                heapq.heappush(
                    hq2,
                    -heapq.heappushpop(hq1, -a),
                )
                nx = -hq1[0]
                s += (nx - x) * (n - 1)
                s -= (nx - x) * (m + 1)

        s += abs(nx - a)



main()
