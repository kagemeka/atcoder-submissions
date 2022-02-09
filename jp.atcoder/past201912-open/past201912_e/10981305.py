import sys

n, q = map(int, sys.stdin.readline().split())
S = [[int(x) for x in sys.stdin.readline().split()] for _ in range(q)]

def main():
    follows = [set() for _ in range(n+1)]
    followed = [set() for _ in range(n+1)]

    for s in S:
        if s[0] == 1:
            a, b = s[1:]
            follows[a].add(b)
            followed[b].add(a)
        else:
            a = s[1]
            if s[0] == 2:
                for f in followed[a]:
                    follows[a].add(f)
                    followed[f].add(a)
            else:
                nex = follows[a].copy()
                for f in follows[a]:
                    for g in follows[f]:
                        nex.add(g)
                        followed[g].add(a)
                follows[a] = nex

    res = [['N'] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j+1 in follows[i+1]:
                res[i][j] = 'Y'

    for s in res:
        yield ''.join(s)

if __name__ == "__main__":
    ans = main()
    print(*ans, sep='\n')
