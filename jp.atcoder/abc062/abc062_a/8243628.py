import sys
input = sys.stdin.readline
print = sys.stdout.write
x, y = [int(_) for _ in input().split()]
a = [4, 6, 9, 11]
if x == 2 or y == 2:
    ans = "No"
elif x in a and y in a:
    ans = "Yes"
elif not x in a and not y in a:
    ans = "Yes"
else:
    ans = "No"

print(ans)
