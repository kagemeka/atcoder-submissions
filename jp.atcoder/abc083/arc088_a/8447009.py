import sys
import math

x, y = [int(x) for x in sys.stdin.readline().split()]

ans = 1 + math.floor(math.log2(y/x))
print(ans)
