import sys

def main():
    n, *w = map(int, sys.stdin.read().split())

    res = set()
    for i in range(n):
        nex = w[i]
        cand = [x for x in res if x >= nex]
        if not cand:
            res.add(nex)
        else:
            res -= set([min(cand)])
            res.add(nex)

    ans = len(res)
    print(ans)

if __name__ == '__main__':
    main()
