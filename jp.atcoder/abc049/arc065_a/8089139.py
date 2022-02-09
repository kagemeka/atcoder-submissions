s = input()

def reverse(string):
  return ''.join(reversed(string))

def split_and_join(string, word):
  return ''.join(string.split(word))

reversed_s = reverse(s)
ls = ["eraser", "dreamer", "erase", "dream"]

for word in ls:
  reversed_word = reverse(word)
  reversed_s = split_and_join(reversed_s, reversed_word)

ans = "YES" if reversed_s == '' else "NO"

print(ans)
