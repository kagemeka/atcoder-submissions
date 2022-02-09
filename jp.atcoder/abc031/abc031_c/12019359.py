import sys
inf = float('inf')

n, *a = map(int, sys.stdin.read().split())

def main():
    se = a.copy(); se = [0] + se
    so = a.copy(); so = [0] + so
    for i in range(0, n - 1, 2): se[i+2] += se[i]
    for i in range(0, n, 2): se[i+1] = se[i]
    for i in range(1, n - 1, 2): so[i+2] += so[i]
    for i in range(1, n, 2): so[i+1] = so[i]

    ans = -inf
    for i in range(1, n + 1):
        score = -inf
        res = None
        for j in range(1, n + 1):
            if i == j: continue
            x, y = i, j
            if x > y: x, y = y, x
            s1 = so[y] - so[x-1]
            s2 = se[y] - se[x-1]
            if s2 > score:
                score, res = s2, s1
        ans = max(ans, res)
    print(ans)

if __name__ ==  '__main__':
    main()
