a, b, c = [int(x) for x in input().split()]

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if c % gcd(a, b) == 0:
    ans = "YES"
else:
    ans = "NO"
print(ans)
