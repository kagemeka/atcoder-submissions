# 2019-11-22 16:25:33(JST)
import sys


def main():
    s = sys.stdin.readline().rstrip()
    n = len(s)

    take_times = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                take_times[i][j] = 0
            elif s[i] == 'U':
                if j < i:
                    take_times[i][j] = 2
                elif j > i:
                    take_times[i][j] = 1
            elif s[i] == 'D':
                if j > i:
                    take_times[i][j] = 2
                elif j < i:
                    take_times[i][j] = 1

    ans = sum(sum(take_times[i]) for i in range(n))
    print(ans)

if __name__ == '__main__':
    main()
