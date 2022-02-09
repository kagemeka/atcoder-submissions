import sys
input = sys.stdin.readline
import collections

n = int(input().rstrip())
a = [a for a in input().split()]

b = collections.deque([], maxlen=n)
for i in range(n):
    b.append(a[i]) if i % 2 == 0 else b.appendleft(a[i])
if (n - 1) % 2 == 0: b = list(reversed(b))

for elem in b: print(elem, end=' ')
