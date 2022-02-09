# 2019-11-25 16:19:29(JST)
import sys
import numpy as np

def main():
    H, W, K = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline().rstrip())
    hw = map(int, sys.stdin.read().split())
    hw = list(zip(hw, hw))

    vert, horiz = np.zeros(H+1, np.int64), np.zeros(W+1, np.int64)
    for h, w in hw:
        vert[h] += 1
        horiz[w] += 1

    cnt_vert = np.bincount(vert[1:], minlength=K+1)
    cnt_horiz = np.bincount(horiz[1:], minlength=K+1)

    # candy i (i = 0...K)個を行から、 K-i個を列から選ぶ選び方の総数。
    # このやり方が今回の肝
    res = (cnt_vert[0:K+1] * cnt_horiz[K::-1]).sum()

    for h, w in hw:
        real_count = vert[h] + horiz[w] - 1
        if real_count == K:
            res += 1
        elif real_count == K - 1:
            res -= 1

    print(res)
if __name__ == '__main__':
    main()
