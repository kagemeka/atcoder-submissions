import sys
input = sys.stdin.readline
import math

n = int(input().rstrip('\n'))
log_floor = math.floor(math.log(n, 2))
res = 0
while True:
    if res == log_floor: print(2 ** res); exit()
    res += 1
