s = input()

for i in range(len(s)):
    if s[i] == 'A':
        a_index = i
        break

for j in range(-1, -(len(s)-a_index), -1):
    if s[j] == 'Z':
        z_index = j
        break

length = (len(s) + z_index) - a_index + 1
print(length)
