s = input()
a = s.index("A")

rs = s[::-1]
z = rs.index("Z")

print(len(s) - a - z)
