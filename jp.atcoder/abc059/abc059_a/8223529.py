strings = input().split()

acronym = ''
for s in strings:
    acronym += s[0].upper()

print(acronym)
