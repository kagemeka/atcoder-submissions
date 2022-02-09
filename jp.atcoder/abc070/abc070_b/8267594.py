from sys import stdin

a, b, c, d = map(int, stdin.readline().rstrip().split())

start = a if a >= c else c
end = b if b <= d else d

print((end - start) if end >= start else 0)
