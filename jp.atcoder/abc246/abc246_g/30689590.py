import typing
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    # binary search score
    # mark the node which have the score more than or equal to fixed value as 'to-remove'.

    # if the node itself is not 'to-remove', and it has more than one 'to-remove' nodes, then it is also 'to-remove'.

    n = int(input())
    a = [-1] + list(map(int, input().split()))
    g: typing.List[typing.List[int]] = [[] for _ in range(n)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    def binary_search() -> int:
        lo, hi = 0, 1 << 30
        while hi - lo > 1:
            score = (lo + hi) >> 1
            if possible(score):
                lo = score
            else:
                hi = score
        return lo

    def possible(score: int) -> bool:
        to_guard = [x >= score for x in a]

        queue = [(0, -1, 1)]
        for u, parent, guardner_count in queue:
            for v in g[u]:
                if v == parent or not to_guard[v]:
                    continue
                if not guardner_count:
                    return True
                guardner_count -= 1
            for v in g[u]:
                if v == parent:
                    continue
                queue.append((v, u, guardner_count + 1))
        return False

    print(binary_search())


if __name__ == "__main__":
    main()
