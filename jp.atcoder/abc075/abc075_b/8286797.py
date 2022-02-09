import sys
from collections import deque

h, w = (int(x) for x in sys.stdin.readline().split())
strings = deque(sys.stdin.read().split())

for i in range(h):
    strings[i] = ''.join(['-', strings[i], '-'])
strings.append('-' * (w + 2)); strings.appendleft('-' * (w + 2))

ans = []
for i in range(1, h + 1):
    s = ''
    for j in range(1, w + 1):
        current = strings[i][j]
        if current == '#': s += '#'
        elif current == '.':
            count = 0
            for t in range(i-1, i+2):
                for u in range(j-1, j+2):
                    if strings[t][u] == '#': count += 1
            s += str(count)
    ans.append(s)

for s in ans: print(s)
