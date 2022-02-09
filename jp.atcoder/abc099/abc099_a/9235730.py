import sys

n = int(sys.stdin.readline().rstrip())

def main():
    return 'ABC' if n < 1000 else 'ABD'

if __name__ == '__main__':
    ans = main()
    print(ans)
