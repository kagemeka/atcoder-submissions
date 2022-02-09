from sys import stdin
n, k = (int(x) for x in stdin.read().split())

displayed = 1
for _ in range(n):
    if displayed <= k: displayed *= 2
    else: displayed += k

print(displayed)
