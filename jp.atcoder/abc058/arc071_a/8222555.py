n = int(input())
strings = [input() for _ in range(n)]

chars = []
for s in strings:
    chars += list(set(s))

used_in_all = []
for c in set(chars):
    if chars.count(c) == n:
        used_in_all.append(c)

if not used_in_all:
    print('')
    exit()

used_in_all.sort()

counts = []

for c in used_in_all:
    for i in range(n):
        count = strings[i].count(c)
        if i == 0:
            m = count
        m = min(m, count)
    counts.append([c, m])

ans = ''
for c, m in dict(counts).items():
    ans += c * m

print(ans)
