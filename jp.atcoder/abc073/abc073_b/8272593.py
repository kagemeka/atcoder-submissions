from sys import stdin

n, *s = (int(x) for x in stdin.read().split())

seats = 0
for l, r in zip(* [iter(s)] * 2):
    seats += r - l + 1

print(seats)
