s = input()

def remove_word_from_string(string, word):
  return ''.join(string.split(word))

ls = ["eraser", "erase", "dreamer", "dream"]

for word in ls:
  s = remove_word_from_string(s, word)

ans = "YES" if s == '' else "NO"

print(ans)
