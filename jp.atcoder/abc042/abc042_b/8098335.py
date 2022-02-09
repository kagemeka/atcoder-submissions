n, l = map(int, input().split())
words = []
for i in range(n):
    words.append(input())
words.sort()

ans = ''.join(words)
print(ans)
