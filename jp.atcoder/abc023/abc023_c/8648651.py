# 2019-11-25 16:19:29(JST)
import sys
import numpy as np

def main():
    H, W, K = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline().rstrip())
    hw = np.array(sys.stdin.read().split(), np.int64)
    h, w = hw[::2], hw[1::2]

    vert = np.bincount(h, minlength=H+1)
    horiz = np.bincount(w, minlength=H+1)

    cnt_vert = np.bincount(vert[1:], minlength=K+1)
    cnt_horiz = np.bincount(horiz[1:], minlength=K+1)

    # candy i (i = 0...K)個を行から、 K-i個を列から選ぶ選び方の総数。
    # このやり方が今回の肝
    res = (cnt_vert[0:K+1] * cnt_horiz[K::-1]).sum()

    # ただしこれは、飴があるマスを基点としたときの行の飴の個数と列の飴の個数の重複部分が考慮されていないので、
    # 答えを修正する必要がある
    real_count = vert[h] + horiz[w] - 1
    cnt_real_count = np.bincount(real_count, minlength=K+1) # 本当の数がi(i=1,2,...Kであるものの個数)
    res -= cnt_real_count[K-1]
    res += cnt_real_count[K]

    print(res)
if __name__ == '__main__':
    main()
