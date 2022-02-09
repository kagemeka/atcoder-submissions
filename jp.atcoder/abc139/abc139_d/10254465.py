import sys

n = int(sys.stdin.readline().rstrip())

def main():
    return (1 + n - 1) * (n - 1) // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
