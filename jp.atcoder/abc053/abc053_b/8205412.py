s = input()
a = s.index("A")

rs = ''.join(reversed(s))
z = rs.index("Z")

print(len(s) - a - z)
