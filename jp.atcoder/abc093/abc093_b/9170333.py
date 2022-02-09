import sys

a, b, k = map(int, sys.stdin.readline().split())

def main():
    if k >= b - a + 1:
        res = list(range(a, b+1))
    else:
        res = set(range(a, a+k)) | set(range(b, b-k, -1))
        res = sorted(res)
    return res

if __name__ == '__main__':
    ans = main()
    print(*ans, sep='\n')
