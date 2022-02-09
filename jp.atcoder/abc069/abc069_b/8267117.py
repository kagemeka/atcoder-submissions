from sys import stdin
s = stdin.readline().rstrip()
print(''.join([s[0], str(len(s) - 2), s[-1]]))
