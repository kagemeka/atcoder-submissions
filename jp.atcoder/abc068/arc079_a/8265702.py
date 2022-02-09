n, m, *ab = [int(x) for x in open(0).read().split()]

from_1, to_n = [], []
for a, b in zip(*[iter(ab)] * 2):
    if a == 1: from_1.append(b)
    elif b == n: to_n.append(a)
for b in from_1:
    if b in to_n: print('POSSIBLE'); exit()
print('IMPOSSIBLE')
