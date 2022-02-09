import sys
import bisect
bi_l = bisect.bisect_left
import collections


s, t = sys.stdin.read().split()
if set(t) - set(s):
    print(-1)
    sys.exit()

n = len(s)

c = collections.defaultdict(list)
for i in range(n):
    c[s[i]].append(i)

i = 0
for ch in t:
    p = c[ch][bi_l(c[ch], (i+1) % n) % len(c[ch])]
    if p <= i % n:
        i += n - i % n + p
    else:
        i += p - i % n
print(i+1) # indexの関係で0から始まっているため
