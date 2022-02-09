from sys import stdin

s, t = stdin.read().split()
s = list(s)

possible_indexes = []
for i in range(len(s) - len(t) + 1):
    substring = s[i: i+len(t)]
    for j in range(len(t)):
        if substring[j] == t[j] or substring[j] == '?': continue
        else: break
    else:
        possible_indexes.append(i)

if not possible_indexes: print('UNRESTORABLE'); exit()

ma = max(possible_indexes)
for j in range(len(t)):
    s[ma+j] = t[j]

s = ''.join(s)

s = s.replace('?', 'a')
print(s)
