mod = 10 ** 7 + 1
N = int(input())
A = [int(a) for a in input().split()]
A.sort()

if N % 2 != 0:
    for i in range(0, N, 2):
        if A[i] != i:
            print(0)
            exit()
    order_count = 2 ** ((N - 1) // 2) % mod

else:
    for i in range(1, N, 2):
        if A[i] != i + 1:
            print(0)
            exit()
    order_count = 2 ** (N // 2) % mod

print(order_count)
