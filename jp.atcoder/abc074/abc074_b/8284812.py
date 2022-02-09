from sys import stdin
n, k, *x = (int(i) for i in stdin.read().split())
total_dist = 0
for i in range(n): total_dist += min(x[i], k - x[i]) * 2
print(total_dist)
