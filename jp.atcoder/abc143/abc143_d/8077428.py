from bisect import bisect_left
n = int(input())
ls = list(map(int, input().split()))
ls.sort()
count = 0
for i in range(n - 2):
  for j in range(i + 1, n - 1):
    bi = bisect_left(ls, ls[i] + ls[j])
    count += bi - j - 1
print(count)
