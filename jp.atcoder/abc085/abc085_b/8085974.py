import bisect
n = int(input())
ls = []
for i in range(n):
  bisect.insort(ls, int(input()))

layer = 1
current = ls[0]
for i in range(n):
  if current != ls[i]:
    layer += 1
    current = ls[i]

print(layer)
