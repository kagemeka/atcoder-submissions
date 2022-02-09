from sys import stdin

n, *a = (int(x) for x in stdin.read().split())

count = {i: 0 for i in set(a)}
for i in a: count[i] += 1

suite_count = count.copy()
for i in count:
    if i - 1 in count: suite_count[i] += count[i-1]
    if i + 1 in count: suite_count[i] += count[i+1]

print(max(suite_count.values()))
