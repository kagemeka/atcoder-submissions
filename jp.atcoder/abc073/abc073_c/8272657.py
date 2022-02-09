from sys import stdin

n, *a = (int(x) for x in stdin.read().split())

count = 0
for n in set(a):
    if a.count(n) % 2 == 1: count += 1

print(count)
