import sys
from bisect import bisect_left as bi_l

n = int(sys.stdin.readline().rstrip())
I = list(zip(*[map(int, sys.stdin.read().split())] * 2))
red = I[:n]
blue = I[n:]

def main():
    red.sort(key=lambda x: x[0])
    blue.sort(key=lambda x: x[0])
    a = []
    b = []
    for x, y in red:
        a.append(x)
        b.append(y)

    paired = [False] * n
    cnt = 0
    for c, d in blue:
        pair = None
        res = -1
        for i in range(bi_l(a, c)):
            if not paired[i] and b[i] < d and b[i] > res:
                pair = i
                res = b[i]
        if not pair is None:
            paired[pair] = True
            cnt += 1

    return cnt

if __name__ == '__main__':
    ans = main()
    print(ans)
