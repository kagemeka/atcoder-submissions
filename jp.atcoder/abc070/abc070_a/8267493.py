from sys import stdin

n = stdin.readline().rstrip()
print('Yes' if n == ''.join(reversed(n)) else 'No')

# need to have reversed object convert into a str by using join method.
