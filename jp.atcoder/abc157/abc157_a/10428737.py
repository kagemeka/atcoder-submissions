import sys

n = int(sys.stdin.readline().rstrip())

def main():
    return (n + 2 - 1) // 2

if __name__ == '__main__':
    ans = main()
    print(ans)
