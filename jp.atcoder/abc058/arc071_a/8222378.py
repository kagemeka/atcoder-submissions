import string

n = int(input())
strings = [input() for _ in range(n)]
alphabets = [a for a in string.ascii_lowercase]

counts = []
for a in alphabets:
    for i in range(n):
        count = strings[i].count(a)
        if i == 0:
            m = count
        m = min(m, count)
    counts.append((a, m))
print(counts)

ans = ''
for count in counts:
    ans += count[0] * count[1]

print(ans)
