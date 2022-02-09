import sys

n, k = map(int, sys.stdin.readline().split())
*v, = map(int, sys.stdin.readline().split())

def main():
    m = min(n, k)
    sl = [None] * (m + 1); sl[0] = 0
    sr = [None] * (m + 1); sr[0] = 0
    neg_l = [None] * (m + 1); neg_l[0] = []
    neg_r = [None] * (m + 1); neg_r[0] = []
    for i in range(m):
        l = v[i]
        r = v[-(i+1)]
        sl[i+1] = sl[i] + l
        sr[i+1] = sr[i] + r

        neg_l[i+1] = neg_l[i].copy()
        if l < 0:
            neg_l[i+1].append(l)
        neg_r[i+1] = neg_r[i].copy()
        if r < 0:
            neg_r[i+1].append(r)

    res = 0
    for i in range(m+1):
        for j in range((m-i)+1):
            s = sl[i]+ sr[j]
            neg = sorted(neg_l[i] + neg_r[j])[:m-(i+j)]
            s -= 0 if not neg else sum(neg)
            res = max(res, s)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
