import sys
from itertools import accumulate

n, W, *wv = map(int, sys.stdin.read().split())
wv = list(zip(*[iter(wv)] * 2))

def main():
    wv.sort(key=lambda x: x[0])
    min_w = wv[0][0]

    items = [[] for _ in range(4)]

    for w, v in wv:
        items[w-min_w].append(v)

    for i in range(4):
        items[i].sort(reverse=True)
        items[i].insert(0, 0)
        items[i] = list(accumulate(items[i]))

    res = 0
    s0 = items[0]
    s1 = items[1]
    s2 = items[2]
    s3 = items[3]
    for i in range(len(s0)):
        v0 = s0[i]
        for j in range(len(s1)):
            v1 = s1[j]
            for k in range(len(s2)):
                v2 = s2[k]
                for l in range(len(s3)):
                    v3 = s3[l]
                    if (j + 2*k + 3*l) + min_w * (i+j+k+l) <= W:
                        res = max(res, v0+v1+v2+v3)

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
