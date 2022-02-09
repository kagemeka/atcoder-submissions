import sys

n = int(sys.stdin.readline().rstrip())
a = [None] + [int(x) for x in sys.stdin.readline().split()]
b = [None] + [int(x) for x in sys.stdin.readline().split()]
c = [None] + [int(x) for x in sys.stdin.readline().split()]

def main():
    res = 0
    for i in range(1, n+1):
        j = a[i]
        res += b[j]
        if a[i-1] == j - 1:
            res += c[j-1]

    return res

if __name__ == '__main__':
    ans = main()
    print(ans)
