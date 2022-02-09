s = input()

def reverse(string):
  return ''.join(reversed(string))

def split_and_join(string, word):
  return ''.join(string.split(word))

s_r = reverse(s)
ls = ["eraser", "erase", "dreamer", "dream"]
ls_r = []
for item in ls:
  ls_r.append(reverse(item))

for word_r in ls_r:
  s_r = split_and_join(s_r, word_r)

ans = "YES" if s_r == '' else "NO"

print(ans)
