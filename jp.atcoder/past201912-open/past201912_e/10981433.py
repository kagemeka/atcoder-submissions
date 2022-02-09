import sys

n, q = map(int, sys.stdin.readline().split())
S = [[int(x) for x in sys.stdin.readline().split()] for _ in range(q)]

def main():
    follows = [set() for _ in range(n+1)]
    for s in S:
        if s[0] == 1:
            a, b = s[1:]
            follows[a].add(b)
        else:
            a = s[1]
            if s[0] == 2:
                for i in range(1, n+1):
                    if i != a:
                        if a in follows[i]:
                            follows[a].add(i)

            else:
                nex = follows[a].copy()
                for i in follows[a]:
                    nex |= follows[i]
                follows[a] = nex - set([a])

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
