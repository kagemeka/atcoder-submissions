n = int(input())
ls = []
for i in range(n):
  ls.append(int(input()))

ls.sort()
layer = 1
current = ls[0]
for i in range(n):
  if current != ls[i]:
    layer += 1
    current = ls[i]

print(layer)
