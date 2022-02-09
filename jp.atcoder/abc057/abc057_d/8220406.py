from statistics import mean
n, a, b = [int(_) for _ in input().split()]
values = [int(v) for v in input().split()]
values.sort(reverse=True)
maximum_mean = mean(values[:a])
print(maximum_mean)

min_value = values[:a][-1]
accepted = values[:a].count(min_value)
full = values.count(min_value)

# def cmb(n, r):
#     if n - r < r: r = n - r
#     if r == 0: return 1
#     if r == 1: return n

#     numerator = [n - r + k + 1 for k in range(r)]
#     denominator = [k + 1 for k in range(r)]

#     for p in range(2,r+1):
#         pivot = denominator[p - 1]
#         if pivot > 1:
#             offset = (n - r) % p
#             for k in range(p-1,r,p):
#                 numerator[k - offset] /= pivot
#                 denominator[k] /= pivot

#     result = 1
#     for k in range(r):
#         if numerator[k] > 1:
#             result *= int(numerator[k])

#     return result
nCr = {}
def cmb(n, r):
    if n < r:
        return 0
    if r == 0 or r == n: return 1
    if r == 1: return n
    if (n,r) in nCr: return nCr[(n,r)]
    nCr[(n,r)] = cmb(n-1,r) + cmb(n-1,r-1)
    return nCr[(n,r)]



if min_value == maximum_mean:
    ans = 0
    for r in range(a, b+1):
        ans += cmb(full, r)
else:
    ans = cmb(full, accepted)

print(ans)
