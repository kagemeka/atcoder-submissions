# 2019-11-28 00:55:58(JST)
import sys
import numpy as np

def main():
    n = int(sys.stdin.readline().rstrip())
    ab = np.array(sys.stdin.read().split(), dtype=np.int64)
    a = ab[:n]
    b = ab[n:]

    res = np.sort(a - b)
    if res.sum() < 0:
        print(-1)
        sys.exit()

    negative_cnt = np.sum(res < 0)
    if not negative_cnt:
        print(0)
        sys.exit()

    negative_sum = np.sum(res[:negative_cnt])
    positive_cnt = 0
    for i in range(n-1, -1, -1):
        negative_sum += res[i]
        positive_cnt += 1
        if negative_sum >= 0:
            break
    cnt = positive_cnt + negative_cnt

    print(cnt)

if __name__ == '__main__':
    main()
