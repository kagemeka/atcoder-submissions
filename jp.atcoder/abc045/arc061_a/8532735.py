import sys
import itertools

s = sys.stdin.readline().rstrip()
n = len(s)


ans = 0
for i in range(n):
    combs = list(map(list, itertools.combinations(range(1, n), i)))
    res2 = 0
    for c in combs:
        c.insert(0, 0); c.append(n)
        print(c)
        res1 = 0
        for j in range(1, i+2):
            res1 += int(s[c[j-1]:c[j]])
            print(int(s[c[j-1]:c[j]]))
        res2 += res1
    ans += res2

print(ans)
