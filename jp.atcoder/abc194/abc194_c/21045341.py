import sys
import numpy as np


buf = sys.stdin.buffer

n = int(
  buf.readline().rstrip()
)

a = np.array(
  buf.readline().split(),
  dtype=np.int64,
)



s0 = a.sum()
s1 = (a ** 2).sum()

s_i_j = (n - 1) * s1
s_ij = (s0 ** 2 - s1) // 2

res = (s_i_j - 2 * s_ij)
print(res)
