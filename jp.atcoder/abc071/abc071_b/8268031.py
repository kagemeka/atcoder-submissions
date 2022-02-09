from sys import stdin
from string import ascii_lowercase
s = stdin.readline().rstrip()
not_used = sorted(set(ascii_lowercase) - (set(s) & set(ascii_lowercase)))
print(not_used[0] if not_used else 'None')
