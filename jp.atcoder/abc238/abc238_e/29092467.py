import typing
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    # DP

    n, q = map(int, input().split())
    known = [False] * (n + 1)
    known[0] = True
    lr = [tuple(map(int, input().split())) for _ in range(q)]
    lr.sort()
    stack = [[] for _ in range(n + 1)]

    def dfs(i: int) -> None:
        if known[i]:
            return
        known[i] = True
        while stack[i]:
            j = stack[i].pop()
            dfs(j)

    for l, r in lr:
        if known[l - 1]:
            dfs(r)
        if known[r]:
            dfs(l - 1)
        if known[l - 1]:
            continue
        stack[l - 1].append(r)
        stack[r].append(l - 1)
        # known_l = known[r]
        # known_r = known[l - 1]
        # known[l - 1] |= known_l
        # known[r] |= known_r

    print("Yes" if known[-1] else "No")


if __name__ == "__main__":
    main()
