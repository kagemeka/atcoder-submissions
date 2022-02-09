import itertools

n, a = map(int, input().split())
integers = list(int(x) - a for x in input().split())
count = 0
for i in range(1, len(integers)+1):
    for combs in itertools.combinations(integers, i):
        av = sum(combs) / i
        if av == 0:
            count += 1

print(count)
