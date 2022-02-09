import sys
def main():
    n, m = map(int, sys.stdin.readline().split())
    xy = map(int, sys.stdin.read().split())
    xy = list(zip(xy, xy))
    G = [set() for _ in range(n)]
    for x, y in xy:
        G[x-1].add(y-1)
        G[y-1].add(x-1)

    res = 0
    for comb in range(2 ** n):
        cand = set()
        for i in range(n):
            if not comb >> i & 1:
                continue
            if cand & G[i] != cand:
                break
            cand.add(i)
        else:
            res = max(res, len(cand))
    print(res)

if __name__ == '__main__':
    main()
