import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n = int(input())
    childs = [[] for _ in range(n)]
    for i in range(1, n):
        parent = int(input()) - 1
        childs[parent].append(i)

    def sarary(u: int) -> int:
        value = 1
        if not childs[u]:
            return value
        child_sararies = [sarary(v) for v in childs[u]]
        return value + max(child_sararies) + min(child_sararies)

    print(sarary(0))


if __name__ == "__main__":
    main()
