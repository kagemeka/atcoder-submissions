import sys
input = sys.stdin.readline

n, m = [int(x) for x in input().split()]
ab = [tuple(int(x) for x in input().split()) for _ in range(m)]

ab = [may for may in ab if may[0] == 1 or may[1] == n]
ab.sort()
ab_end_n = [may for may in ab if may[1] == n]

for m in ab:
    if m[0] == 1:
        if (m[1], n) in ab_end_n: print('POSSIBLE'); exit()
        else:
            continue
    else:
        break
print('IMPOSSIBLE')
