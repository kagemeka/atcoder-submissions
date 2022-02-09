import sys

n, k, *v = map(int, sys.stdin.read().split())

def main():
    m = min(n, k)
    ls = [None] * (m + 1)
    rs = [None] * (m + 1)
    l_neg = [None] * (m + 1)
    r_neg = [None] * (m + 1)

    ls[0] = 0
    rs[0] = 0
    l_neg[0] = []
    r_neg[0] = []

    for i in range(m):
        l = v[i]; r = v[-(i+1)]
        ls[i+1] = ls[i] + l
        rs[i+1] = rs[i] + r

        l_neg[i+1] = l_neg[i].copy()
        if l < 0:
            l_neg[i+1].append(l)
        r_neg[i+1] = r_neg[i].copy()
        if r < 0:
            r_neg[i+1].append(r)

    res = 0
    for i in range(m+1):
        for j in range((m-i)+1):
            s = ls[i] + rs[j]
            neg = sorted(l_neg[i] + r_neg[j])
            s -= sum(neg[:k-(i+j)])
            res = max(res, s)
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
