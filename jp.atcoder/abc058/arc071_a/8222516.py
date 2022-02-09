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

accepted_chars_of_each_string = [[c for c in s if c in used_in_all] for s in strings]
counts = dict([(c, 0) for c in used_in_all])

for c in used_in_all:
    for i in range(n):
        count = strings[i].count(c)
        if i == 0:
            m = count
        m = min(m, count)
    counts[c] = m

ans = ''
for c, m in counts.items():
    ans += c * m

print(ans)
