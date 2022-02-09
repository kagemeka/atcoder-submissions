import sys

MOD = 10 ** 9 + 7

n = int(sys.stdin.readline().rstrip())
s1, s2 = sys.stdin.read().split()

def main():
    if s1[0] == s2[0]:
        i = 1
        res = 3
        flag = 0
    else:
        i = 2
        res = 6
        flag = 1

    while i < n:
        if s1[i] == s2[i]:
            if flag:
                res *= 1
            else:
                res = res * 2 % MOD
            flag = 0
            i += 1
        else:
            if flag:
                res = res * 3 % MOD
            else:
                res = res * 2 % MOD
            flag = 1
            i += 2
    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
