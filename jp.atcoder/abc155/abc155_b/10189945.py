import sys

n, *A = map(int, sys.stdin.read().split())

def main():
    for a in A:
        if a % 2 == 0:
            if a % 3 == 0 or a % 5 == 0:
                continue
            else:
                return 'DENIED'
    return 'APPROVED'

if __name__ == '__main__':
    ans = main()
    print(ans)
