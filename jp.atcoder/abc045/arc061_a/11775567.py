import sys

s = sys.stdin.readline().rstrip()
n = len(s)

def c(n):
    return pow(2, max(0, n - 1))

def main():
    res = 0
    for l in range(n):
        for r in range(l, n):
            res += int(s[l:r+1]) * c(l) * c(n - 1 - r)
    print(res)

if __name__ ==  '__main__':
    main()
