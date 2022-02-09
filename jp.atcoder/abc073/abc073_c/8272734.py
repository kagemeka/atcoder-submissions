from sys import stdin

n, *a = (int(x) for x in stdin.read().split())

each_count = {n: 0 for n in set(a)}


for n in a:
    each_count[n] += 1

count = 0
for v in each_count.values():
    if v % 2 == 1: count += 1

print(count)
