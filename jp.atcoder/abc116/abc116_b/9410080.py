import sys

def f(n):
    if n & 1:
        return n * 3 + 1
    else:
        return n // 2

s = int(sys.stdin.readline().rstrip())

def main():
    a = s
    res = set([a])
    for i in range(2, 10**6+1):
        a = f(a)
        if a in res:
            return i
        res.add(a)

if __name__ == '__main__':
    ans = main()
    print(ans)
