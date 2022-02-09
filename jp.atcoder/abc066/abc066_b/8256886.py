import sys
input = sys.stdin.readline

s = input().rstrip()     # rstrip() がないとダメ
if len(s) % 2 == 1: s = s[:-1]
else: s = s[:-2]

for _ in range(len(s) // 2):
    if s.count(s[:len(s) // 2]) == 2: print(len(s));  exit()
    else: s = s[:-2]
print(0)
