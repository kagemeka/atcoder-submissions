import sys

n = int(sys.stdin.readline().rstrip())
*s, = sys.stdin.read().split()

def main(s):
    res = []
    for j in range(n):
        t = ''
        for i in range(n-1, -1, -1):
            t += s[i][j]
        res.append(t)

    return res

if __name__ == '__main__':
    ans = main(s)
    print(*ans, sep='\n')
