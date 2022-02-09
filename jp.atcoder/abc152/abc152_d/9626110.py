import sys

n = sys.stdin.readline().rstrip()
len_n = len(n)
m = n[1:-1]
m = int(m) if m else 0
l = int(n[0])
r = int(n[-1])
n = int(n)

def main():
    res = [[0] * 10 for _ in range(10)]

    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                if i <= n:
                    res[i][j] += 1
            for k in range(len_n-2+1):
                if k < len_n - 2:
                    res[i][j] += 10 ** k
                else:
                    if i < l:
                        res[i][j] += 10 ** k
                    elif i == l:
                        if j <= r:
                            res[i][j] += m + 1
                        else:
                            res[i][j] += m
                    else:
                        pass

    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans += res[i][j] * res[j][i]
    return ans

if __name__ == '__main__':
    ans = main()
    print(ans)
