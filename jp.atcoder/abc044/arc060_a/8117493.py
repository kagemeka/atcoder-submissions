import itertools

n, a = map(int, input().split())
integers = list(map(int, input().split()))
count = 0
for i in range(1, len(integers)+1):
    for combs in itertools.combinations(integers, i):
        av = sum(combs) / i
        if av == a:
            count += 1

print(count)
