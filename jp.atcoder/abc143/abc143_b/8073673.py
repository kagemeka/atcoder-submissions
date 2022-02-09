n = int(input())
del = list(map(int, input().split()))
sum = 0
i = 0

while i < n - 1:
  k = i
  while k < n - 1:
    k += 1
    sum += del[i] * del[k]
  i += 1

print(sum)
