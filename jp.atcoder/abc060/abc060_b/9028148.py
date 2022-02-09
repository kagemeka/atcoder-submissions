import sys

a, b, c = map(int, sys.stdin.readline().split())

def main():
    for i in range(a, a * b, a):
        if i % b == c:
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    ans = main()
    print(ans)
