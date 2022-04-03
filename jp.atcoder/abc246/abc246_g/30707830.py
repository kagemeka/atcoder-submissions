import typing
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
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

        # at least how many guardners needed be inherited?

        to_inherit = [0] * n

        queue = [0]
        parent = [-1] * n
        for u in queue:
            for v in g[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                queue.append(v)

        stack = [0]
        while stack:
            u = stack.pop()
            if u < 0:
                u = ~u
                if to_inherit[u] > 0:
                    to_inherit[u] -= 1
                if parent[u] != -1:
                    to_inherit[parent[u]] += to_inherit[u]
                continue
            stack.append(~u)
            for v in g[u]:
                if v == parent[u]:
                    continue
                to_inherit[u] += to_guard[v]
                stack.append(v)

        return to_inherit[0] > 0

    print(binary_search())


if __name__ == "__main__":
    main()
