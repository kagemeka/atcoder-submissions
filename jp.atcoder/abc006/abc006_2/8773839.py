import sys
sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline().rstrip())

MOD = 10 ** 4 + 7

def tribonacci(N):
    if N == 0:
        return 0,0,1
    a,b,c = F(N//2)
    a,b,c,d,e = a*a,2*a*b,2*a*c+b*b,2*b*c,c*c
    b += a; c += a; d += a
    c += b; d += b; e += b
    a,b,c = c,d,e
    if N&1:
        a,b,c = b+a,c+a,a
    a %= MOD; b %= MOD; c %= MOD
    return a,b,c

ans = tribonacci(N)[2]
print(ans)
