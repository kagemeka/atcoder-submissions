from sys import stdin

n = stdin.readline().rstrip()
print('Yes' if n == reversed(n) else 'No')
