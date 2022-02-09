#                         author:  kagemeka
#                         created: 2019-11-07 13:42:36(JST)
import sys
# import collections
import math
# import string
# import bisect
# import re
# import itertools
# import statistics
# import functools
# import operator


def main():
    x = int(sys.stdin.readline().rstrip())

    if x <= 3:
        print(1)
        exit()


    cand = []
    for b in range(math.floor(x ** 0.5), 1, -1):
        bp = b ** math.floor(math.log(x, b))
        cand.append(bp)
    ans = max(cand)
    print(ans)


if __name__ == "__main__":
    # execute only if run as a script
    main()

# アルゴリズムは正しいのでやっぱりlogにバグがありそう
# 前もlog使った時に答えが間違ってたことあったきがする
# 近似系の関数を使う時は必ずしも正しい答えにならないみたい
