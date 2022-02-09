import sys
s = [s for s in sys.stdin.readline().rstrip()]

ans = 0
if s[0] == '>':
    count = 1
    i = 1
    while s[i] == '>':
        count += 1
        i += 1
    del s[:i]
    ans += (1 + count) * count // 2

if s[-1] == '<':
    count = 1
    i = -2
    while s[i] == '>':
        count += 1
        i -= 1
    del s[i+1:]
    ans += count
    (1 + count) * count // 2

s.append(None)

while s != [None]:
    l_c, r_c = 0, 0
    i = 0
    # if s[i] == '<':
    while s[i] == '<':
        l_c += 1
        i += 1
    del s[:i]

    j = 0
    # if s[j] == '>':
    while s[j] == '>':
        r_c += 1
        j += 1
    del s[:j]

    if l_c >= r_c:
        ans += (1 + l_c) * l_c // 2 + r_c * (r_c - 1) // 2
    else:
        ans += l_c * (l_c - 1) // 2 + (1 + r_c) * r_c // 2

print(ans)
