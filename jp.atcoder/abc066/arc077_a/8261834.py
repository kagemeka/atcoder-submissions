import sys
input = sys.stdin.readline


n = int(input().rstrip())
a = [a for a in input().split()]

b = [None] * n
for i in range(n):
    if i % 2 == 0: b[n // 2 + i // 2] = a[i]
    else: b[n // 2 - (-(-i // 2))] = a[i]
if (n - 1) % 2 == 0: b = list(reversed(b))

for elem in b: print(elem, end=' ')
