from bisect import bisect_left

n = input()
ls = list(map(int, input().split()))
count = 0
for i in range(0, n - 2):
  for j in range(i + 1, n - 1):
    two_sides_sum = ls[i]+ ls[j]
    for k in range(j + 1, n):
      if two_sides_sum <= ls[k]:
        count += k - j - 1
        break
print(count)
