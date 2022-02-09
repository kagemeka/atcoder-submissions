s = input()

def remove_word_from_string(string, word):
  return ''.join(string.split(word))

# listの順番は、語尾がrのワードを先にしないと最終的にrが残ってしまう
# これだとワードの種類が多くなったときなどに使えなくなってしまうので
# もっと良い方法はないものだろうか...
ls = ["eraser", "erase", "dreamer", "dream"]

for word in ls:
  s = remove_word_from_string(s, word)

ans = "YES" if s == '' else "NO"

print(ans)
