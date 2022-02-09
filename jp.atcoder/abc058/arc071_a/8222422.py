from string import ascii_lowercase

n = int(input())
strings = [input() for _ in range(n)]
alphabets = [a for a in ascii_lowercase]

counts = []
for a in alphabets:
    for i in range(n):
        count = strings[i].count(a)
        if count == 0:
            break
        if i == 0:
            m = count
            continue
        m = min(m, count)
    else:
        counts.append((a, m))

ans = ''
for count in counts:
    ans += count[0] * count[1]

print(ans)
