A, B, C, D = [int(side) for side in input().split()]

S_FIRST = A * B
S_SECOND = C * D
if S_FIRST >= S_SECOND:
    print(S_FIRST)
else:
    print(S_SECOND)
