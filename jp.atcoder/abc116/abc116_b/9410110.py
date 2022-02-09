import sys

def f(n):
    if n & 1:
        return n * 3 + 1
    else:
        return n // 2

s = int(sys.stdin.readline().rstrip())

def main():
    a_m = set([1, 2, 4])
    a = s
    for i in range(1, 10**6-2):
        if a in a_m:
            return i + 3
        a = f(a)

if __name__ == '__main__':
    ans = main()
    print(ans)
