import sys

n = int(sys.stdin.readline().rstrip())

def main():
    ans = (n ** 0.5 // 1) ** 2
    return int(ans)

if __name__ == '__main__':
    ans = main()
    print(ans)
