import typing
import sys
sys.setrecursionlimit(1 << 20)


def main() -> typing.NoReturn:
    n = int(input())
    g = [[] for _ in range(n)]
    for _ in range(n - 1):
        a, b = map(int, input().split())
        g[a].append(b)
        g[b].append(a)



    def dfs(u: int, p: int) -> typing.Tuple[int, bool]:
        ok = []
        cnt = []
        deg = 0
        for v in g[u]:
            if v == p: continue
            c, o = dfs(v, u)
            deg += c >= 1
            if deg < len(cnt):
                assert c == 0
                c = 1
                o = True
                deg += 1
            ok.append(o)
            cnt.append(c)

        s = sum(cnt)
        if u == 0:
            for i in range(len(cnt)):
                if ok[i]: continue
                if deg - (cnt[i] >= 1) >= 1: continue
                s += 1
                break
        return s, deg == len(cnt) >= 1

    print(dfs(0, -1)[0])

main()
