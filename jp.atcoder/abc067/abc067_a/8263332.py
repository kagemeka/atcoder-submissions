import sys
input = sys.stdin.readline

a, b = [int(x) for x in input().split()]
ans = "Possible" if (a + b) % 3 == 0 else 'Impossible'
print(ans)
