import sys
input = sys.stdin.readline

X, A, B = [int(i) for i in input().split()]

if A >= B: print('delicious')
elif B - A >= X: print('safe')
else: print('dangerous')
