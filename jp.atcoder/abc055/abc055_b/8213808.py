mod = int(1e9+7)
n = int(input())

power = 1
for i in range(1, n+1):
    power = power * i % mod
print(power)
