mod = 10 ** 9 + 7
N = int(input())
A = [int(a) for a in input().split()]

# Nが偶数ならAiは全て奇数、Nが奇数なら Aiは全て偶数でなければならない,なぜなら、2x + Ai = N - 1を満たすxが自然数(非負整数)でなければならないから
# さらに、Nが奇数の時はfor i in range(0, N, 2) において 0が１個、それ以外のiが２個ずつ存在しなければならず(これはAiが全て偶数であることも満たしている)、
# Nが偶数の時はfor i in range(1, N, 2) において 全てのiが２個ずつ存在しなければならない(これはAiがすべて奇数であることも満たしている)
# これを踏まえた上でNが偶数の時は N/2人の位置が決まれば反対側の人の位置も決まり、Nが奇数の時は中央の人は固定として、それ以外 (N-1)/2人の位置が決まれば残りの人は反対側で位置が決まる。それぞれ２通りなので、
# よって
if N % 2 != 0:
    for i in range(0, N, 2):
        if A.count(i) == 2:
            continue
        elif A.count(0) == 1:
            continue
        print(0)
        exit()

    #order_count = 1
    #for i in range((N - 1) // 2):
        order_count = 2 ** ((N - 1) // 2) % mod

else:
    for i in range(1, N, 2):
        if A.count(i) != 2:
            print(0)
            exit()
    #order_count = 1
    #for i in range(N // 2):
        order_count = 2 ** (N // 2) % mod

print(order_count)
