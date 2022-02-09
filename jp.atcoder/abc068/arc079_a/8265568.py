import sys
from collections import deque
l = deque(sys.stdin.readlines())
n, m = (int(x) for x in l[0].split())
l.popleft()
ab = deque()
for i in range(m):
  a, b = tuple(int(x) for x in l[i].split())
  if a == 1 or b == n: ab.append((a, b))

for i in ab:
  if i[0] == 1:
      if (i[1], n) in ab: print('POSSIBLE'); exit()

print('IMPOSSIBLE')
