s = input()
ls = [char for char in s]
while True:
    if ls[0] != 'A':
        ls.pop(0)
    else:
        break
while True:
    if ls[-1] != 'Z':
        ls.pop(-1)
    else:
        break

print(len(ls))
