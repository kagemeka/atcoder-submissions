import sys
lines = sys.stdin.readlines()

h, w = [int(x) for x in lines[0].split()]
lines[0] = '#' * (w + 2)
for i in range(1, h+1):
    lines[i] = '#' + lines[i].rstrip() + '#'
lines.append('#' * (w + 2))

for i in range(h+2):
    print(lines[i])
