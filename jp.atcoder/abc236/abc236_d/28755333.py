import typing
import sys

sys.setrecursionlimit(1 << 20)


def main() -> None:
    n = int(input())
    m = 2 * n
    a = [[0] * m for _ in range(m)]
    for i in range(m - 1):
        a[i][i + 1 :] = list(map(int, input().split()))

    def dfs(s: int, i: int, happiness: int) -> int:
        s |= 1 << i
        mx = 0
        k = -1
        for j in range(i + 1, m):
            if s >> j & 1:
                continue
            k = j
            break
        for j in range(i + 1, m):
            if s >> j & 1:
                continue
            h = happiness ^ a[i][j]
            t = s | 1 << j
            if t == (1 << m) - 1:
                return h
            if j == k:
                for l in range(j + 1, m):
                    if s >> l & 1:
                        continue
                    mx = max(mx, dfs(t, l, h))
                    break
            else:
                mx = max(mx, dfs(t, k, h))
        return mx

    print(dfs(0, 0, 0))


if __name__ == "__main__":
    main()
