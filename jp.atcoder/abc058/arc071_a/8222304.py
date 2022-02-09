n = int(input())
chars_of_each_string = [[char for char in input()] for _ in range(n)]

chars = []
for characters in chars_of_each_string:
    chars += list(set(characters))

chars_used_in_all = []
for char in set(chars):
    if chars.count(char) == n:
        chars_used_in_all.append(char)

if not chars_used_in_all:
    print('')
    exit()

chars_used_in_all.sort()

accepted_chars_of_each_string = [[char for char in chars if char in chars_used_in_all] for chars in                                 chars_of_each_string]
each_count = dict([(char, 0) for char in chars_used_in_all])

for char in chars_used_in_all:
    for i in range(n):
        count = accepted_chars_of_each_string[i].count(char)
        if i == 0:
            min_count = count
        min_count = min(min_count, count)
    each_count[char] = min_count

res = ''
for char, count in each_count.items():
    res += char * count

print(res)
