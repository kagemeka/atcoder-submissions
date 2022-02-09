# 2019-11-14 20:54:46(JST)
import sys
# import collections
# import math
# from string import ascii_lowercase, ascii_uppercase, digits
# from bisect import bisect_left as bi_l, bisect_right as bi_r
import itertools
# from functools import reduce
# import operator as op
# from scipy.misc import comb # float
# import numpy as np

def main():
    n, k = [int(x) for x in sys.stdin.readline().split()]
    # ある１地点を経由してそれ以外の全てにいくのが最も多く
    # これは (n - 1) * (n - 2) // 2　通り
    # kがこれより大きいときには存在せず、それ以下の時は理論上存在する
    if k > (n - 1) * (n - 2) // 2:
        print(-1)
        sys.exit()

    all_uv = list(itertools.combinations(range(1, n+1), 2))

    m = n * (n - 1) // 2 - k
    print(m)
    # 1を中央として考えて、最低限1以外のn-1個の頂点は1とつながっている状態である必要がある
    for u, v in all_uv[:m]: # kの制約から、iの最大値は最小で(n-1)-1まで
        print(u, v)


if __name__ == "__main__":
    main()
