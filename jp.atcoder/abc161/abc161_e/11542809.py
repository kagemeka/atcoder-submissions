import sys

inf = float('inf')
n, k, c = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().rstrip()

def main():
    dp_l = [[0] * 2 for _ in range(n + 2)]
    for i in range(n):
        dp_l[i+1][0] = max(dp_l[i][0], dp_l[i][1])
        if s[i] == 'o':
            if i + 1 - c < 0:
                dp_l[i+1][1] = 1
            else:
                dp_l[i+1][1] = dp_l[i+1-c][0] + 1
    dp_r = [[0] * 2 for _ in range(n + 2)]
    for i in range(n, 0, -1):
        dp_r[i][0] = max(dp_r[i+1][0], dp_r[i+1][1])
        if s[i-1] == 'o':
            if i + c > n + 1:
                dp_r[i][1] = 1
            else:
                dp_r[i][1] = dp_r[i+c][0] + 1

    for i in range(1, n + 1):
        if s[i-1] == 'o':
            if dp_l[i][0] + dp_r[i][0] < k:
                print(i)

if __name__ ==  '__main__':
    main()
