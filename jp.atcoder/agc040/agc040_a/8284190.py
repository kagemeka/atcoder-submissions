import sys
from collections import deque
s = deque(s for s in sys.stdin.readline().rstrip())

s.append(None)
ans = 0
while s[0] != None:
    l_c = 0
    while s[0] == '<':
        l_c += 1
        s.popleft()

    r_c = 0
    while s[0] == '>':
        r_c += 1
        s.popleft()

    if l_c >= r_c:
        ans += (1 + l_c) * l_c // 2 + r_c * (r_c - 1) // 2
    else:
        ans += l_c * (l_c - 1) // 2 + (1 + r_c) * r_c // 2

print(ans)
