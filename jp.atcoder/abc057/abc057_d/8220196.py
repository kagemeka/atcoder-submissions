from statistics import mean
n, a, b = [int(_) for _ in input().split()]
values = [int(v) for v in input().split()]
values.sort(reverse=True)
maximum_mean = mean(values[:a])
print(maximum_mean)

min_value = values[:a][-1]
accepted = values[:a].count(min_value)
full = values.count(min_value)

def cmb(n, r):
    if n - r < r: r = n - r
    if r == 0: return 1
    if r == 1: return n

    numerator = [n - r + k + 1 for k in range(r)]
    denominator = [k + 1 for k in range(r)]

    for p in range(2,r+1):
        pivot = denominator[p - 1]
        if pivot > 1:
            offset = (n - r) % p
            for k in range(p-1,r,p):
                numerator[k - offset] /= pivot
                denominator[k] /= pivot

    result = 1
    for k in range(r):
        if numerator[k] > 1:
            result *= int(numerator[k])

    return result


print(cmb(full, accepted))
