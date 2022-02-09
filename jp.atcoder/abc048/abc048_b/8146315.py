a, b, x = map(int, input().split())

def f(n, x):
    if n < 0:   # a == 0
        return 0
    elif n == 0:
        return 1
    elif n < x:
        return 0
    else:
        return n // x

count = f(b, x) - f(a-1, x)

print(count)
