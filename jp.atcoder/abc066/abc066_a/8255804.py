import sys
input = sys.stdin.readline

price = [int(p) for p in input().split()]
price.sort()
print(price[0] + price[1])
