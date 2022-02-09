import sys
input = sys.stdin.readline

s = input()
if len(s) == len(set(s)):
    print('yes')
else:
    print('no')
