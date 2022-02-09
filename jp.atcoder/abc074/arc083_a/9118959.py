import sys

A, B, C, D, E, F = map(int, sys.stdin.readline().split())
E = 100 * E / (100 + E)

def main():
    w = set()
    for w1 in range(0, F+1, 100*A):
        for w2 in range(0, F-w1+1, 100*B):
            w.add(w1 + w2)

    s = set()
    for s1 in range(0, F+1, C):
        for s2 in range(0, F-s1+1, D):
            s.add(s1 + s2)

    w = sorted(w)
    s = sorted(s)

    res = set()
    for i in w[1:]:
        for j in s:
            if i + j > F:
                break
            sol = 100 * j / (i + j)
            if sol <= E:
                res.add((sol, i+j, j))

    res = sorted(res, reverse=True)
    return res[0][1], res[0][2]

if __name__ == '__main__':
    ans = main()
    print(*ans, sep=' ')
