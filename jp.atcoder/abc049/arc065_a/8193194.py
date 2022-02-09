s = input()
words = ['dream', 'dreamer', 'erase', 'eraser']
words = sorted(words, reverse=True)
print()
for word in words:
    if word in s:
        s = s.replace(word, "")

if not s:
    ans = "YES"
else:
    ans = "NO"

print(ans)
