a, b, x = map(int, input().split())
ls = list(range(a, b+1))
count = [i % x for i in ls].count(0)

print(count)
