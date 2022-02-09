import sys

n = int(sys.stdin.readline().rstrip())

def main():
    return 111 * ((n + 111 - 1) // 111)

if __name__ == '__main__':
    ans = main()
    print(ans)
