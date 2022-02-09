import sys
input = sys.stdin.readline

rgb = int(''.join(input().split()))

if rgb % 4 == 0:
    print("YES")
else:
    print("NO")
